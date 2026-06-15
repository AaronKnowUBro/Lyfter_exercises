from actions import (
    add_students,
    view_students,
    view_top_students,
    view_global_average,
    delete_student,
    view_failed_students
)
from data import export_data, import_data

def show_menu(students):
    while True:
        print("\n--- Student Management System ---")
        print("1. Add students")
        print("2. View all students")
        print("3. View top 3 students")
        print("4. View global average")
        print("5. Export data to CSV")
        print("6. Import data from CSV")
        print("7. Delete student")
        print("8. View failed students")
        print("9. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            print()
            add_students(students)
        elif choice == "2":
            print()
            view_students(students)
        elif choice == "3":
            print()
            view_top_students(students)
        elif choice == "4":
            print()
            view_global_average(students)
        elif choice == "5":
            print()
            export_data(students)
        elif choice == "6":
            print()
            import_data(students)
        elif choice == "7":
            print()
            delete_student(students)
        elif choice == "8":
            print()
            view_failed_students(students)
        elif choice == "9":
            print("\nExiting program...\n")
            break
        else:
            print("\nInvalid option.\n")