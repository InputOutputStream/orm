from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import Base, Notes, Etudiant, Discipline, Promoted, Field
from conn import con_url

try:
    # Create database engine
    engine = create_engine(con_url)
except Exception as e:
    print("Error: Failed to connect to DB server")

def moyenne(notes):
    
    if not notes:
        return 0
    
    sn = 0
    tn = 0
    for note in notes:
            print(f"Code: {note.code}, Nom: {note.nom}, Note: {note.note}, Coef: {note.coef}")
            sn += note.coef
            tn += note.coef * note.note

    return tn / sn if sn != 0 else 0

def drop_existing():
    Base.metadata.drop_all(bind=engine)

def setup_database():
    Base.metadata.create_all(bind=engine)

def get_session():
    Session = sessionmaker(bind=engine)
    return Session()

def add_student(session):
    try:
        id = int(input("Enter student ID: "))
        nom = input("Enter student name: ")
        prenom = input("Enter student last name: ")
        age = int(input("Enter student age: "))
        new_student = Etudiant(id=id, nom=nom, prenom=prenom, age=age)
        session.add(new_student)
        session.commit()
        print("Student added successfully!")
    except Exception as e:
        print(e)
        
def display_students(session):
    students = session.query(Etudiant).all()
    print("List of students:")
    for student in students:
        print(f"ID: {student.id}, Name: {student.nom}, Last Name: {student.prenom}, Age: {student.age}")

def update_student(session):
    try:
        id = int(input("Enter student ID to update: "))
        student = session.query(Etudiant).filter_by(id=id).first()
        if student:
            new_age = int(input("Enter new age: "))
            student.age = new_age
            session.commit()
            print("Student age updated successfully!")
        else:
            print("Student not found!")
    except Exception as e:
            print(e)
        
def delete_student(session):
    try:
        id = int(input("Enter student ID to delete: "))
        student = session.query(Etudiant).filter_by(id=id).first()
        if student:
            session.delete(student)
            session.commit()
            print("Student deleted successfully!")
        else:
            print("Student not found!")
    except Exception as e:
            print(e)
        
def add_subject_mark(session):
    try:
        id = int(input("Enter student ID: "))
        code = int(input("Enter Subject ID: "))
        nom_ue = input("Enter Subject name: ")
        note = float(input("Enter student mark: "))
        coef = int(input("Enter coefficient: "))
        student = session.query(Etudiant).filter_by(id=id).first()
        if student:
            notes = Notes(code=code, nom=nom_ue, note=note, coef=coef, etudiant_id=id)
            session.add(notes)
            session.commit()
            print("Subject mark added successfully!")
        else:
            print("Student not found")
    except Exception as e:
            print(e)
       
def print_student_average(session):
    try:
        id = int(input("Enter student ID: "))
        student = session.query(Etudiant).filter_by(id=id).first()
        if student:
            notes = session.query(Notes).filter_by(etudiant_id=id).all()
            if notes:
                avg = moyenne(notes)
                print(f"Average grade for {student.nom} = {avg}")
            else:
                print("No grades found for this student.")
        else:
            print("Student not found")
    except Exception as e:
        print(e)
       
def promote_student(session):
    try:
        id = int(input("Enter student ID: "))
        code = int(input("Enter Promotion ID: "))
        student = session.query(Etudiant).filter_by(id=id).first()
        notes = session.query(Notes).filter_by(etudiant_id=id).all()
        grade = None

        if student and notes:
            avg = moyenne(notes)
            if avg >= 17:
                grade = "Excellent"
            elif avg >= 15:
                grade = "Very Good"
            elif avg >= 12:
                grade = "Good"
            elif avg >= 10:
                grade = "Fair"
            else:
                print("Cannot promote student")
            
            if grade:
                promo = Promoted(code=code, grade=grade, etudiant_id=id)
                session.add(promo)
                session.commit()
                print("Student promoted successfully!")
        else:
            print("Student or grades not found")
    except Exception as e:
            print(e)
       
def send_to_disciplinary(session):
    try:
        id = int(input("Enter student ID: "))
        reason = input("Enter fault: ")
        code = int(input("Enter the council code: "))
        student = session.query(Etudiant).filter_by(id=id).first()
        if student:
            dc = Discipline(code=code, reason=reason, etudiant_id=id)
            session.add(dc)
            session.commit()
            print("Student sent to Disciplinary Council")
        else:
            print("Student not found")
    except Exception as e:
            print(e)
       
def direct_student_field(session):
    try:
        id = int(input("Enter student ID: "))
        field_name = input("Enter the field name: ")
        reason = input("Reason for proposal: ")
        grade = input("Enter the student's grade: ")
        student = session.query(Etudiant).filter_by(id=id).first()
        if student:
            field_change = Field(field_name=field_name, grade=grade, reason=reason, etudiant_id=id)
            session.add(field_change)
            session.commit()
            print("Student directed towards a particular field")
        else:
            print("Student not found")
    except Exception as e:
            print(e)
       