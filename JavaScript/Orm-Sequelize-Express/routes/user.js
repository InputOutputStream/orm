const express = require('express');
const { Etudiant } = require('../models');

const router = express.Router();

// Create a user
router.post('/add_user', async (req, res) => {
  const { nom, matricule, age } = req.body;
  try {
    const newUser = await Etudiant.create({ nom, matricule, age});
    res.status(201).json({ message: 'User added successfully', user: newUser });
  } catch (error) {
    res.status(400).json({ error: error.message });
  }
});



// Read all users
router.get('/users', async (req, res) => {
  try {
    const users = await Etudiant.findAll();
    res.json(users);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

// Update a user
router.put('/update_user/:id', async (req, res) => {
  const { id } = req.params;
  const { nom, matricule, age} = req.body;
  try 
  {
    const user = await Etudiant.findByPk(id);

    if (!user) {
      return res.status(404).json({ error: 'User not found' });
    }

    user.nom = nom || user.nom; // Update the user name 
    user.matricule = matricule || user.matricule; // Update the email
    user.age = age || user.age // Update age
    await user.save(); // Commit changes
    res.json({ message: 'User updated successfully', user });
  } catch (error) {
    res.status(400).json({ error: error.message });
  }
});


// Delete a user
router.delete('/delete_user/:id', async (req, res) => {
  const { id } = req.params;
  try {
    const user = await Etudiant.findByPk(id);
    if (!user) {
      return res.status(404).json({ error: 'User not found' });
    }
    await user.destroy();
    res.json({ message: 'User deleted successfully' });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});


module.exports = router;
