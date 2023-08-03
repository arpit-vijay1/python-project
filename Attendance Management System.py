
students_data = {}
attendance_data = []

def add_student():
    roll_no = int(input("Enter Roll No: "))
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    address = input("Enter Address: ")
    students_data[roll_no] = {"name": name, "age": age, "address": address}
    print("Student with Roll No {} added successfully!".format(roll_no))

def update_student():
    roll_no = int(input("Enter Roll No of student to update: "))
    if roll_no in students_data:
        name = input("Enter New Name: ")
        age = int(input("Enter New Age: "))
        address = input("Enter New Address: ")
        students_data[roll_no] = {"name": name, "age": age, "address": address}
        print("Student with Roll No {} updated successfully!".format(roll_no))
    else:
        print("Student with Roll No {} not found!".format(roll_no))

def delete_student():
    roll_no = int(input("Enter Roll No of student to delete: "))
    if roll_no in students_data:
        del students_data[roll_no]
        print("Student with Roll No {} deleted successfully!".format(roll_no))
    else:
        print("Student with Roll No {} not found!".format(roll_no))

def mark_attendance():
    roll_no = int(input("Enter Roll No of student to mark attendance: "))
    if roll_no in students_data:
        attendance_status = input("Mark attendance as Present (P) or Absent (A): ").upper()
        if attendance_status == "P":
            attendance_data.append((roll_no, "Present"))
            print("Attendance marked as Present for student with Roll No {}.".format(roll_no))
        elif attendance_status == "A":
            attendance_data.append((roll_no, "Absent"))
            print("Attendance marked as Absent for student with Roll No {}.".format(roll_no))
        else:
            print("Invalid attendance status. Please enter 'P' for Present or 'A' for Absent.")
    else:
        print("Student with Roll No {} not found!".format(roll_no))

def view_attendance():
    if not attendance_data:
        print("Attendance Data is empty.")
        return

    print("Attendance Data:")
    for roll_no, attendance_status in attendance_data:
        if roll_no in students_data:
            print("Roll No: {}, Name: {}, Attendance: {}".format(
                roll_no, students_data[roll_no]['name'], attendance_status
            ))
        else:
            print("Roll No: {} (Student not found)".format(roll_no))

def generate_report():
    total_students = len(students_data)
    total_attendance = len(attendance_data)
    attendance_percentage = (total_attendance / total_students) * 100

    print("Attendance Report:")
    print("Total Students: {}".format(total_students))
    print("Total Attendance: {}".format(total_attendance))
    print("Attendance Percentage: {:.2f}%".format(attendance_percentage))

    print("\nIndividual Student Reports:")
    for roll_no, student_info in students_data.items():
        student_attendance = [status for rn, status in attendance_data if rn == roll_no]
        student_total_attendance = len(student_attendance)
        student_attendance_percentage = (student_total_attendance / total_attendance) * 100
        print("Roll No: {}, Name: {}, Attendance Percentage: {:.2f}%".format(
            roll_no, student_info['name'], student_attendance_percentage
        ))

def view_all_students():
    print("All Students Details:")
    for roll_no, student_info in students_data.items():
        print("Roll No: {}, Name: {}, Age: {}, Address: {}".format(
            roll_no, student_info['name'], student_info['age'], student_info['address']
        ))

def main():
    admin_username = "admin"
    admin_password = "password"

    entered_username = input("Enter admin username: ")
    entered_password = input("Enter admin password: ")

    if entered_username == admin_username and entered_password == admin_password:
        while True:
            print("\nAttendance Management System")
            print("1. Student Information")
            print("2. Mark Attendance")
            print("3. View Attendance")
            print("4. Generate Report")
            print("5. View All Students")
            print("6. Exit")

            choice = int(input("Enter your choice: "))

            if choice == 1:
                while True:
                    print("\nStudent Information")
                    print("1. Add Student")
                    print("2. Update Student")
                    print("3. Delete Student")
                    print("4. Back")

                    sub_choice = int(input("Enter your choice: "))
                    if sub_choice == 1:
                        add_student()
                    elif sub_choice == 2:
                        update_student()
                    elif sub_choice == 3:
                        delete_student()
                    elif sub_choice == 4:
                        break
                    else:
                        print("Invalid choice.")

            elif choice == 2:
                mark_attendance()

            elif choice == 3:
                view_attendance()

            elif choice == 4:
                generate_report()

            elif choice == 5:
                view_all_students()

            elif choice == 6:
                print("Exiting...")
                break

    else:
        print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()