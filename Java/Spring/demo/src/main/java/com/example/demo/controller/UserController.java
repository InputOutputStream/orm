package com.example.demo.controller;

import com.example.demo.exception.ResourceNotFoundException;
import com.example.demo.model.Etudiant;
import com.example.demo.repository.UserRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/etudiants")
public class UserController {

    @Autowired
    private UserRepository userRepository;

    // Create a user
    @PostMapping
    public Etudiant createUser(@RequestBody Etudiant user) {
        return userRepository.save(user);
    }

    // Read all users
    @GetMapping
    public List<Etudiant> getAllUsers() {
        return userRepository.findAll();
    }

    // Read a single user
    @GetMapping("/{id}")
    public ResponseEntity<Etudiant> getUserById(@PathVariable Long id) {
        Etudiant user = userRepository.findById(id)
                .orElseThrow(() -> new ResourceNotFoundException("User not found with id " + id));
        return ResponseEntity.ok(user);
    }

    // Update a user
    @PutMapping("/{id}")
    public ResponseEntity<Etudiant> updateUser(@PathVariable Long id, @RequestBody Etudiant userDetails) {
        Etudiant user = userRepository.findById(id)
                .orElseThrow(() -> new ResourceNotFoundException("User not found with id " + id));

        user.setNom(userDetails.getNom());
        user.setPrenom(userDetails.getPrenom());
        user.setAge(userDetails.getAge());

        Etudiant updatedUser = userRepository.save(user);
        return ResponseEntity.ok(updatedUser);
    }

    // Delete a user
    @DeleteMapping("/{id}")
    public ResponseEntity<Void> deleteUser(@PathVariable Long id) {
        Etudiant user = userRepository.findById(id)
                .orElseThrow(() -> new ResourceNotFoundException("User not found with id " + id));

        userRepository.delete(user);
        return ResponseEntity.noContent().build();
    }
}
