from sqlalchemy import Integer, String, Column, ForeignKey, Float
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Etudiant(Base):
    __tablename__ = 'etudiants'
    
    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String, unique=False, index=True)
    prenom = Column(String, unique=False, index=False)
    age = Column(Integer, unique=False, index=True)
    
    # Relations One-to-Many with the other classes
    notes = relationship('Notes', back_populates='etudiant')
    disciplines = relationship('Discipline', back_populates='etudiant')
    promotions = relationship('Promoted', back_populates='etudiant')
    fields = relationship('Field', back_populates='etudiant')

class Notes(Base):
    __tablename__ = 'notes'
    
    code = Column(Integer, primary_key=True, index=True)
    nom = Column(String, unique=False, index=True)
    note = Column(Float, unique=False, index=False)  # Use Float for grades
    coef = Column(Integer, unique=False, index=True)
    
    # Many-to-One relation with the Etudiant class
    etudiant_id = Column(Integer, ForeignKey('etudiants.id'))
    etudiant = relationship('Etudiant', back_populates='notes')

class Discipline(Base):
    __tablename__ = 'discipline'
    
    code = Column(Integer, primary_key=True, index=True)
    reason = Column(String, unique=False, index=True)
    
    # Many-to-One relation with the Etudiant class
    etudiant_id = Column(Integer, ForeignKey('etudiants.id'))
    etudiant = relationship('Etudiant', back_populates='disciplines')

class Promoted(Base):
    __tablename__ = 'promoted'
    
    code = Column(Integer, primary_key=True, index=True)
    grade = Column(String, unique=False, index=True)
    
    # Many-to-One relation with the Etudiant class
    etudiant_id = Column(Integer, ForeignKey('etudiants.id'))
    etudiant = relationship('Etudiant', back_populates='promotions')


class Field(Base):
    __tablename__ = 'field'
    
    id = Column(Integer, primary_key=True, index=True)  # Add primary key column
    field_name = Column(String, unique=False, index=True)
    grade = Column(String, unique=False, index=True)
    reason = Column(String, unique=False, index=True)
    
    # Many-to-One relation with the Etudiant class
    etudiant_id = Column(Integer, ForeignKey('etudiants.id'))
    etudiant = relationship('Etudiant', back_populates='fields')
