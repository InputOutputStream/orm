const express = require('express');
const bodyParser = require('body-parser');
const userRoutes = require('./routes/user');
const { syncDatabase } = require('./models');

const app = express();
const port = 5000;

app.use(bodyParser.json());

// Use user routes
app.use('/', userRoutes);

// Sync the database and start the server
syncDatabase()
  .then(() => {
  app.listen(port, () => {
    console.log(`Server running at http://localhost:${port}`);
  });
}).catch((error) => {
  console.error('Unable to sync database:', error);
});
