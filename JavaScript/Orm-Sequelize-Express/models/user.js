const { DataTypes } = require('sequelize');
const sequelize = require('../config/database');

const Etudiant = sequelize.define('Etudiant', {
  nom: {
    type: DataTypes.STRING,
    allowNull: false,
    unique: true,
  },
  matricule: {
    type: DataTypes.STRING,
    allowNull: false,
    unique: true,
  },
  age:{
    type: DataTypes.INTEGER,
    allowNull: false,
    unique: true,
  },
  
});

module.exports = Etudiant;
