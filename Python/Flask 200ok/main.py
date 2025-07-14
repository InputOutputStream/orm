import requests

BASE_URL = 'http://localhost:5000'

# Helper function to print responses from API calls
def print_response(response):
    print(f"Status Code: {response.status_code}")
    print("Response:")
    print(response.json())
    print("--------------------------------------------------------------------------\n")

# Test all cases
def test_all():
    # Add a new student
    print("1. Add a new student")
    student_data = {
        "nom": "Smith",
        "prenom": "John",
        "age": 20
    }
    
    student_data2 = {
        "nom": "Frank",
        "prenom": "Twitter",
        "age": 25
    }
    
    student_data3 = {
        "nom": "Maxou",
        "prenom": "Twitter",
        "age": 25
    }
    response = requests.post(f"{BASE_URL}/add_student", json=student_data)
    print_response(response)

    response = requests.post(f"{BASE_URL}/add_student", json=student_data2)
    print_response(response)

    response = requests.post(f"{BASE_URL}/add_student", json=student_data3)
    print_response(response)

    # Display all students
    print("2. Display all students")
    response = requests.get(f"{BASE_URL}/students")
    print_response(response)

    # Update a student's info
    print("3. Update a student's info")
    student_id = 1  # Assuming the student ID to update
    update_data = {
        "prenom": "Jane",
        "age": 21
    }
    response = requests.put(f"{BASE_URL}/update_student/{student_id}", json=update_data)
    print_response(response)

    # Dismiss a student
    print("4. Dismiss a student")
    student_id = 1  # Assuming the student ID to dismiss
    response = requests.delete(f"{BASE_URL}/dismiss_student/{student_id}")
    print_response(response)

    # Add a subject mark for a student
    print("5. Add a subject mark for a student")
    student_id = 2  # Assuming the student ID to add a mark
    mark_data = {
        "code": 101,
        "nom_ue": "Mathematics",
        "note": 15.5,
        "coef": 2
    }
    response = requests.post(f"{BASE_URL}/add_subject_mark/{student_id}", json=mark_data)
    print_response(response)

    # Print student average
    print("6. Print student average")
    student_id = 2 # Assuming the student ID to get average
    response = requests.get(f"{BASE_URL}/student_average/{student_id}")
    print_response(response)

    # Promote a student
    print("7. Promote a student")
    student_id = 2  # Assuming the student ID to promote
    response = requests.post(f"{BASE_URL}/promote_student/{student_id}")
    print_response(response)

    # Send a Student to Disciplinary Council
    print("8. Send a Student to Disciplinary Council")
    student_id = 2  # Assuming the student ID to send to council
    council_data = {
        "reason": "Misconduct in class",
        "code": 1111
    }
    response = requests.post(f"{BASE_URL}/disciplinary_council/{student_id}", json=council_data)
    print_response(response)

    # Direct a student towards a particular field
    print("9. Direct a student towards a particular field")
    student_id = 2  # Assuming the student ID to direct to a field
    field_data = {
        "field_name": "Engineering",
        "grade": "A",
        "reason": "Student's interest in engineering"
    }
    response = requests.post(f"{BASE_URL}/direct_to_field/{student_id}", json=field_data)
    print_response(response)

    # QUIT
    print("0. QUIT")
    print("Exiting test cases.")

if __name__ == '__main__':
    test_all()
