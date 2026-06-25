# A basic version for a student's fee status

fee_paid = {"A": "Yes",
             "B": "No",
               "C": "Yes",
                 "D": "No",
                   "E": "Yes",
                     "F": "No"}
                     
                     

student = input("Enter the name of the student: ").strip().upper()


if student in fee_paid:
    if fee_paid[student] == "Yes":
        print("The student has paid the fee.")
    else:
        print("The student has not paid the fee.")
else:
    print("Student not found.")
