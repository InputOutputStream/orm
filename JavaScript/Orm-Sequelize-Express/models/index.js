const sequelize = require('../config/database');
const User = require('./user');

const syncDatabase = async () => {
  await sequelize.sync({ force: true }); // no keep old data
  console.log("Database synced!");
};

module.exports = {
  User,
  syncDatabase,
};
