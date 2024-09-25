import redis from 'redis';

const client = redis.createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err}`);
});

// Function to set multiple values in a hash
function setSchoolValues() {
  const key = 'HolbertonSchools';
  const values = {
    Portland: 50,
    Seattle: 80,
    NewYork: 20,
    Bogota: 20,
    Cali: 40,
    Paris: 2,
  };

  for (const [city, value] of Object.entries(values)) {
    client.hset(key, city, value, redis.print);
  }
}

// Function to display the hash
function displayHash() {
  const key = 'HolbertonSchools';
  client.hgetall(key, (err, reply) => {
    if (err) {
      console.error(`Error retrieving hash for ${key}: ${err}`);
    } else {
      console.log(`Hash for ${key}:`, reply);
    }
  });
}

setSchoolValues();
displayHash();

