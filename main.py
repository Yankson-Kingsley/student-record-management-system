students = []


def add_student():
    name = input("Enter student name: ")
    students.append(name)
    print(f"{name} added successfully!")


def view_students():
    print("\nStudent List:")

    if len(students) == 0:
        print("No students found.")

    else:
        for student in students:
            print(student)


def search_student():
    search_name = input("Enter student name to search: ")

    if search_name in students:
        print(f"{search_name} found!")

    else:
        print(f"{search_name} not found.")


def delete_student():
    name = input("Enter student name to delete: ")

    if name in students:
        students.remove(name)
        print(f"{name} deleted successfully!")

    else:
        print(f"{name} not found.")


while True:

    print("\n===== Student Record Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice") 