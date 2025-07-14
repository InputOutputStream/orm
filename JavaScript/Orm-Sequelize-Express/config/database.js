const { Sequelize } = require('sequelize');

const sequelize = new Sequelize('test', 'hge', 'hge', {
  host: 'localhost',
  dialect: 'postgres',
});

sequelize.authenticate().then(()=>{
    console.log("Connection Established Succesfully")
})
  .catch(err =>{
      console.log("Could not connect to database: "+ err)
  })

module.exports = sequelize;
