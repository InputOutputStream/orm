# model.py
from conn import db
from sqlalchemy import Integer, String, Column, ForeignKey, Float
from sqlalchemy.orm import relationship


class Etudiant(db.Model):
    __tablename__ = 'etudiants'
    
    id = db.Column(Integer, primary_key=True, index=True)
    nom = Column(String, unique=False, index=True)
    prenom = Column(String, unique=False, index=False)
    age = Column(Integer, unique=False, index=True)
    
    # Relations One-to-Many with the other classes
    notes = relationship('Notes', back_populates='etudiant')
    disciplines = relationship('Discipline', back_populates='etudiant')
    promotions = relationship('Promoted', back_populates='etudiant')
    fields = relationship('Field', back_populates='etudiant')
    
    def __repr__(self):
        return f'<Etudiant {self.nom}>'


class Notes(db.Model):
    __tablename__ = 'notes'
    
    code = Column(Integer, primary_key=True, index=True)
    nom = Column(String, unique=False, index=True)
    note = Column(Float, unique=False, index=False)  # Use Float for grades
    coef = Column(Integer, unique=False, index=True)
    
    # Many-to-One relation with the Etudiant class
    etudiant_id = Column(Integer, ForeignKey('etudiants.id'))
    etudiant = relationship('Etudiant', back_populates='notes')
    
    def __repr__(self):
        return f'<Notes Code: {self.code}, Nom: {self.nom}, Note: {self.note}, Coef: {self.coef}>'


class Discipline(db.Model):
    __tablename__ = 'discipline'
    
    code = Column(Integer, primary_key=True, index=True)
    reason = Column(String, unique=False, index=True)
    
    # Many-to-One relation with the Etudiant class
    etudiant_id = Column(Integer, ForeignKey('etudiants.id'))
    etudiant = relationship('Etudiant', back_populates='disciplines')
    
    def __repr__(self):
        return f'<Discipline Code: {self.code}, Reason: {self.reason}, Student: {self.etudiant.nom}>'


class Promoted(db.Model):
    __tablename__ = 'promoted'
    
    code = Column(Integer, primary_key=True, index=True)
    grade = Column(String, unique=False, index=True)
    
    # Many-to-One relation with the Etudiant class
    etudiant_id = Column(Integer, ForeignKey('etudiants.id'))
    etudiant = relationship('Etudiant', back_populates='promotions')

    def __repr__(self):
        return f'<Promoted Code: {self.code}, Grade: {self.grade}, Student: {self.etudiant.nom}>'


class Field(db.Model):
    __tablename__ = 'field'
    
    id = Column(Integer, primary_key=True, index=True)  # Add primary key column
    field_name = Column(String, unique=False, index=True)
    grade = Column(String, unique=False, index=True)
    reason = Column(String, unique=False, index=True)
    
    # Many-to-One relation with the Etudiant class
    etudiant_id = Column(Integer, ForeignKey('etudiants.id'))
    etudiant = relationship('Etudiant', back_populates='fields')
    
    def __repr__(self):
        return f'<Field ID: {self.id}, Field Name: {self.field_name}, Reason: {self.reason}, Grade: {self.grade}, Student: {self.etudiant.nom}>'
