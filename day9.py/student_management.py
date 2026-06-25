"""
  Day 9: Student Management System
A clean, beginner-friendly terminal application to manage student records.
Features continuous lookups, specific field updates, and input sanitization.
"""
# Initial student database
students_data = {
    "a": {"class": "10", "grades": "A", "fee_paid": "Yes"},
    "b": {"class": "9", "grades": "B", "fee_paid": "No"},
    "c": {"class": "8", "grades": "A", "fee_paid": "Yes"},
}


def show_menu():
    print("\n====== STUDENT DATA SYSTEM ======")
    print("1. View student class and grades")
    print("2. View fee payment status")
    print("3. Update student information")
    print("4. Switch to a different student")
    print("5. Exit completely")


def show_class_and_grades(student_name):
    print("\n====== CLASS AND GRADES ======")
    print(f"Student Name: {student_name.upper()}")
    print(f"Class:        {students_data[student_name]['class']}")
    print(f"Grades:       {students_data[student_name]['grades']}")


def show_fee_status(student_name):
    print("\n====== FEE PAYMENT STATUS ======")
    status = students_data[student_name]["fee_paid"].strip().capitalize()
    if status == "Yes":
        print("Status: Paid")
    else:
        print("Status: Unpaid / Owed")


def update_student_information(student_name):
    print("\n====== UPDATE OPTIONS ======")
    print("1. Update Class")
    print("2. Update Grades")
    print("3. Update Fee Status")
    
    choice = input("What field would you like to update? (1-3): ").strip()

    if choice == "1":
        new_class = input("Enter new class: ").strip()
        students_data[student_name]["class"] = new_class
        print("Class updated successfully.")
        
    elif choice == "2":
        new_grade = input("Enter new grade: ").strip().upper()
        students_data[student_name]["grades"] = new_grade
        print("Grades updated successfully.")
        
    elif choice == "3":
        new_fee = input("Has the student paid? (Yes/No): ").strip().capitalize()
        students_data[student_name]["fee_paid"] = new_fee
        print("Fee status updated successfully.")
        
    else:
        print("Invalid choice. Returning to main menu without changes.")


# Main Program Loop
while True:
    print("\n=========================================")
    student_name = input("Enter student name (or type 'quit' to exit): ").strip().lower()

    if student_name == "quit":
        print("Thank you for using the Student Data System. Goodbye!")
        break

    if student_name not in students_data:
        print("Error: Student record not found. Please try again.")
        continue

    # Action menu loop for the selected student
    while True:
        show_menu()
        user_choice = input("Enter your choice (1-5): ").strip()

        if user_choice == "1":
            show_class_and_grades(student_name)
            
        elif user_choice == "2":
            show_fee_status(student_name)
            
        elif user_choice == "3":
            update_student_information(student_name)
            
        elif user_choice == "4":
            print(f"Closing record for {student_name.upper()}...")
            break  # Exits back to the student name selection prompt
            
        elif user_choice == "5":
            print("Thank you for using the Student Data System. Goodbye!")
            exit()  # Shuts down the entire script cleanly
            
        else:
            print("Invalid selection. Please enter a number between 1 and 5.")
