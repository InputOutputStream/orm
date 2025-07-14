const Sequelize = require("sequelize");

const sequelize = new Sequelize('test', 'hge', 'hge', 
    {
        dialect: "postgres",
        host: 'localhost',
    }
)


module.exports = sequelize
