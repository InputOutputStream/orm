# app.py
from flask import Flask, jsonify, request
from conn import db, con_url
import model

app = Flask(__name__)

# Configuration for the PostgreSQL database
app.config['SQLALCHEMY_DATABASE_URI'] = con_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database with the Flask app
db.init_app(app)

# Method to calculate average marks
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


# Create the database and tables before each request
@app.before_first_request
def create_tables():
    db.drop_all()
    db.create_all()


# Route to add a new student
@app.route('/add_student', methods=['POST'])
def add_student():
    data = request.json
    nom = data.get('nom')
    prenom = data.get('prenom')
    age = data.get('age')

    if not nom or not prenom or not age:
        return jsonify({"error": "Missing required fields (nom, prenom or age)"}), 400

    new_student = model.Etudiant(nom=nom, prenom=prenom, age=age)
    db.session.add(new_student)
    db.session.commit()

    return jsonify({"message": "Student added successfully"}), 201


# Route to display all students
@app.route('/students', methods=['GET'])
def get_students():
    students = model.Etudiant.query.all()
    return jsonify([{
        "id": student.id,
        "nom": student.nom,
        "prenom": student.prenom,
        "age": student.age
    } for student in students])


# Route to update a student's info
@app.route('/update_student/<int:id>', methods=['PUT'])
def update_student(id):
    student = db.session.get(model.Etudiant, id)


    if not student:
        return jsonify({"error": "Student not found"}), 404

    data = request.json
    if 'nom' in data:
        student.nom = data['nom']
    if 'prenom' in data:
        student.prenom = data['prenom']
    if 'age' in data:
        student.age = data['age']

    db.session.commit()
    return jsonify({"message": "Student updated successfully"}), 200


# Route to dismiss a student
@app.route('/dismiss_student/<int:id>', methods=['DELETE'])
def dismiss_student(id):
    student = db.session.get(model.Etudiant, id)


    if not student:
        return jsonify({"error": "Student not found"}), 404

    db.session.delete(student)
    db.session.commit()
    return jsonify({"message": "Student dismissed successfully"}), 200


# Route to add a subject mark for a student
@app.route('/add_subject_mark/<int:id>', methods=['POST'])
def add_subject_mark(id):
    student = db.session.get(model.Etudiant, id)


    if not student:
        return jsonify({"error": "Student not found"}), 404

    data = request.json
    
    print("/\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ ")
    print(data)
    print("/\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ ")

    if 'code' in data:
        code = data['code']
    if 'nom_ue' in data:
        nom_ue = data['nom_ue']
    if 'note' in data:
        note = data['note']
    if 'coef' in data:
        coef = data['coef']



    if not code or not nom_ue or note is None or coef is None:
        return jsonify({"error": "Missing required fields (code, nom_ue, note, coef)"}), 400

    new_note = model.Notes(code=code, nom=nom_ue, note=note, coef=coef, etudiant_id=id)
    db.session.add(new_note)
    db.session.commit()

    return jsonify({"message": "Subject mark added successfully"}), 201


# Route to print student average
@app.route('/student_average/<int:id>', methods=['GET'])
def get_student_average(id):
    student = db.session.get(model.Etudiant, id)

    if not student:
        return jsonify({"error": "Student not found"}), 404

    notes = model.Notes.query.filter_by(etudiant_id=id).all()
    avg = moyenne(notes)  
    return jsonify({"average": avg})


# Route to promote a student
@app.route('/promote_student/<int:id>', methods=['POST'])
def promote_student(id):
    student = db.session.get(model.Etudiant, id)

    if not student:
        return jsonify({"error": "Student not found"}), 404

    notes = model.Notes.query.filter_by(etudiant_id=id).all()
    avg = moyenne(notes)  
    grade = None
    
    if avg >= 10: 
        if avg >= 17:
            grade = "Excellent"
        elif avg >= 15:
            grade = "Very Good"
        elif avg >= 12:
            grade = "Good"
        else:
            grade="fair"
            
        promo = model.Promoted(grade=grade, etudiant_id=id)
        db.session.add(promo)
        db.session.commit()
        return jsonify({"message": "Student promoted successfully"}), 200
    else:
        return jsonify({"message": "Student not eligible for promotion"}), 400


# Route to send a student to disciplinary council
@app.route('/disciplinary_council/<int:id>', methods=['POST'])
def disciplinary_council(id):
    student = db.session.get(model.Etudiant, id)

    if not student:
        return jsonify({"error": "Student not found"}), 404

    data = request.json
    if 'reason' in data:
        reason = data['reason']
    if 'code' in data:
        code = data['code']

    if not reason or not code:
        return jsonify({"error": "Missing required fields (reason or code)"}), 400

    discipline = model.Discipline(reason=reason, code=code, etudiant_id=id)
    db.session.add(discipline)
    db.session.commit()

    return jsonify({"message": "Student sent to disciplinary council successfully"}), 201


# Route to direct a student towards a particular field
@app.route('/direct_to_field/<int:id>', methods=['POST'])
def direct_to_field(id):
    student = db.session.get(model.Etudiant, id)

    if not student:
        return jsonify({"error": "Student not found"}), 404

    data = request.json
    if 'field_name' in data:
        field_name = data['field_name']
    if 'grade' in data:
        grade = data['grade']
    if "reason" in data:
        reason = data['reason']

    if not field_name or not grade or not reason:
        return jsonify({"error": "Missing required fields (field_name, grade, reason)"}), 400

    field = model.Field(field_name=field_name, grade=grade, reason=reason, etudiant_id=id)
    db.session.add(field)
    db.session.commit()

    return jsonify({"message": "Student directed to field successfully"}), 201


if __name__ == '__main__':
    app.run(debug=True)
