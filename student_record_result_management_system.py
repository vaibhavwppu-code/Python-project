# Student Record and Result Management System
# Python Project

# Subjects
subjects = ("Python", "Maths", "English")

# Student data
students = []
roll_numbers = set()


# Function to add student
def add_student():

    roll = input("Enter Roll Number: ")

    if roll in roll_numbers:
        print("Roll number already exists!")
        return

    name = input("Enter Student Name: ")

    marks = {}

    for subject in subjects:

        while True:

            try:
                m = float(input("Enter marks in " + subject + ": "))

                if m >= 0 and m <= 100:
                    marks[subject] = m
                    break
                else:
                    print("Enter marks between 0 and 100")

            except ValueError:
                print("Please enter numbers only")
                continue

    student = {
        "roll": roll,
        "name": name,
        "marks": marks
    }

    students.append(student)
    roll_numbers.add(roll)

    print("Student added successfully!")


# Function to display all students
def view_students():

    if len(students) == 0:
        print("No student records found")
        return

    print("\n----- Student Records -----")

    for s in students:

        print("\nRoll Number:", s["roll"])
        print("Name:", s["name"])

        for subject in subjects:
            print(subject, ":", s["marks"][subject])

        total = sum(s["marks"].values())
        percentage = total / len(subjects)

        print("Total Marks:", total)
        print("Percentage:", round(percentage, 2))


# Function to search student
def search_student():

    roll = input("Enter Roll Number: ")

    for s in students:

        if s["roll"] == roll:

            print("\nStudent Found")
            print("Name:", s["name"])
            print("Roll Number:", s["roll"])
            print("Marks:", s["marks"])

            return

    print("Student not found")


# Function to update student
def update_student():

    roll = input("Enter Roll Number: ")

    for s in students:

        if s["roll"] == roll:

            print("1. Update Name")
            print("2. Update Marks")

            choice = input("Enter choice: ")

            if choice == "1":

                name = input("Enter new name: ")
                s["name"] = name
                print("Name updated")

            elif choice == "2":

                for subject in subjects:

                    while True:

                        try:
                            m = float(input("Enter new marks in " + subject + ": "))

                            if m >= 0 and m <= 100:
                                s["marks"][subject] = m
                                break
                            else:
                                print("Invalid marks")

                        except ValueError:
                            print("Enter a valid number")

                print("Marks updated")

            else:
                print("Invalid choice")

            return

    print("Student not found")


# Function to delete student
def delete_student():

    global students

    roll = input("Enter Roll Number: ")

    for s in students:

        if s["roll"] == roll:

            students.remove(s)
            roll_numbers.remove(roll)

            print("Student deleted successfully")
            return

    print("Student not found")


# Function to calculate result
def calculate_result():

    roll = input("Enter Roll Number: ")

    for s in students:

        if s["roll"] == roll:

            total = sum(s["marks"].values())
            percentage = total / len(subjects)

            print("\n----- Student Result -----")
            print("Name:", s["name"])
            print("Roll Number:", s["roll"])

            print("Total Marks:", total)
            print("Percentage:", round(percentage, 2), "%")

            if percentage >= 90:
                grade = "A+"
            elif percentage >= 80:
                grade = "A"
            elif percentage >= 70:
                grade = "B"
            elif percentage >= 60:
                grade = "C"
            elif percentage >= 40:
                grade = "D"
            else:
                grade = "F"

            print("Grade:", grade)

            if percentage >= 40:
                print("Result: PASS")
            else:
                print("Result: FAIL")

            return

    print("Student not found")


# Function to sort students
def sort_students():

    if len(students) == 0:
        print("No records available")
        return

    students.sort(
        key=lambda s: sum(s["marks"].values()),
        reverse=True
    )

    print("\nStudents sorted by marks")

    for s in students:

        total = sum(s["marks"].values())
        percentage = total / len(subjects)

        print(s["name"], "-", round(percentage, 2), "%")


# Function to display topper
def display_topper():

    if len(students) == 0:
        print("No records available")
        return

    topper = max(
        students,
        key=lambda s: sum(s["marks"].values())
    )

    total = sum(topper["marks"].values())
    percentage = total / len(subjects)

    print("\n----- Class Topper -----")
    print("Name:", topper["name"])
    print("Roll Number:", topper["roll"])
    print("Total Marks:", total)
    print("Percentage:", round(percentage, 2), "%")


# Function to show class summary
def class_summary():

    if len(students) == 0:
        print("No records available")
        return

    total_marks = []

    for s in students:

        total = sum(s["marks"].values())
        percentage = total / len(subjects)

        total_marks.append(percentage)

    average = sum(total_marks) / len(total_marks)

    print("\n----- Class Summary -----")
    print("Total Students:", len(students))
    print("Class Average:", round(average, 2), "%")
    print("Highest Percentage:", max(total_marks))
    print("Lowest Percentage:", min(total_marks))


# Main Menu
def main():

    while True:

        print("\n================================")
        print("   STUDENT MANAGEMENT SYSTEM")
        print("================================")

        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Calculate Result")
        print("7. Sort Students")
        print("8. Display Topper")
        print("9. Class Summary")
        print("10. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            update_student()

        elif choice == "5":
            delete_student()

        elif choice == "6":
            calculate_result()

        elif choice == "7":
            sort_students()

        elif choice == "8":
            display_topper()

        elif choice == "9":
            class_summary()

        elif choice == "10":
            print("Thank you!")
            break

        else:
            print("Invalid choice! Try again")


# Program starts here
if __name__ == "__main__":
    main()
