from metier import *

def main():
    drop_existing()
    setup_database()
    session = get_session()
    
    while True:
        print("--------------------------------------------------------------------------\n")
        print("1. Add a new student")
        print('2. Display all students')
        print("3. Update a student's info")
        print("4. Dismiss a student")
        print("5. Add a subject mark for a student")
        print("6. Print student average")
        print("7. Promote a student")
        print("8. Send a Student to Disciplinary Council")
        print("9. Direct a student towards a particular field among the available ones")
        print("0. QUIT")
        
        try:
            choice = int(input("Enter a choice: "))
        except Exception as e:
            print("Invalid value for choice integer")
        
        if choice == 0:
            break
        elif choice == 1:
            add_student(session)
        elif choice == 2:
            display_students(session)
        elif choice == 3:
            update_student(session)
        elif choice == 4:
            delete_student(session)
        elif choice == 5:
            add_subject_mark(session)
        elif choice == 6:
            print_student_average(session)
        elif choice == 7:
            promote_student(session)
        elif choice == 8:
            send_to_disciplinary(session)
        elif choice == 9:
            direct_student_field(session)
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
