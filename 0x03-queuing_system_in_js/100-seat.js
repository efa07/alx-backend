import express from 'express';
import { promisify } from 'util';
import redis from 'redis';
import kue from 'kue';

const app = express();
const port = 1245;
const client = redis.createClient();
const queue = kue.createQueue();

let reservationEnabled = true;

// Function to reserve seats
const reserveSeat = (number) => {
  client.set('available_seats', number);
};

// Function to get current available seats
const getCurrentAvailableSeats = async () => {
  const getAsync = promisify(client.get).bind(client);
  const seats = await getAsync('available_seats');
  return seats ? parseInt(seats, 10) : 0;
};

// Set initial available seats
reserveSeat(50);

// Route to get available seats
app.get('/available_seats', async (req, res) => {
  const availableSeats = await getCurrentAvailableSeats();
  res.json({ numberOfAvailableSeats: availableSeats.toString() });
});

// Route to reserve a seat
app.get('/reserve_seat', async (req, res) => {
  if (!reservationEnabled) {
    return res.json({ status: 'Reservations are blocked' });
  }
  const job = queue.create('reserve_seat').save((err) => {
    if (err) {
      return res.json({ status: 'Reservation failed' });
    }
    return res.json({ status: 'Reservation in process' });
  });
});

// Process the queue
queue.process('reserve_seat', async (job, done) => {
  const currentSeats = await getCurrentAvailableSeats();
  if (currentSeats <= 0) {
    reservationEnabled = false;
    return done(new Error('Not enough seats available'));
  }
  reserveSeat(currentSeats - 1);
  console.log(`Seat reservation job ${job.id} completed`);
  done();
});

// Route to process the queue
app.get('/process', async (req, res) => {
  res.json({ status: 'Queue processing' });
  queue.process('reserve_seat', async (job, done) => {
    const currentSeats = await getCurrentAvailableSeats();
    if (currentSeats <= 0) {
      reservationEnabled = false;
      return done(new Error('Not enough seats available'));
    }
    reserveSeat(currentSeats - 1);
    console.log(`Seat reservation job ${job.id} completed`);
    done();
  });
});

// Start the server
app.listen(port, () => {
  console.log(`Server running on http://localhost:${port}`);
});

