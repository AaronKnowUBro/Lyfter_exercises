def is_valid_name(name):
    return name.replace(" ", "").isalpha()

def is_valid_section(section):
    return len(section) == 3 and section[:2].isdigit() and section[2].isalpha()

def student_exists(students, name, section):
    return any(s["name"] == name and s["section"] == section for s in students)

def get_valid_grade(subject):
    while True:
        try:
            grade = float(input(f"Enter grade for {subject} (0-100): "))
            if 0 <= grade <= 100:
                return grade
            else:
                print("Grade must be between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def add_students(students):
    while True:
        try:
            n = int(input("How many students do you want to add? "))
            if n > 0:
                break
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    for _ in range(n):
        while True:
            name = input("Enter full name: ").strip()
            section = input("Enter section (e.g., 11B): ").strip()

            if not is_valid_name(name):
                print("Invalid name. Must not contain numbers or be empty.")
                continue
            if not is_valid_section(section):
                print("Invalid section format. Example: 11B")
                continue
            if student_exists(students, name, section):
                print("Student already exists.")
                continue

            spanish = get_valid_grade("Spanish")
            english = get_valid_grade("English")
            social = get_valid_grade("Social Studies")
            science = get_valid_grade("Science")

            student = {
                "name": name,
                "section": section,
                "spanish": spanish,
                "english": english,
                "social": social,
                "science": science,
                "average": (spanish + english + social + science) / 4
            }
            students.append(student)
            print("\nStudent added successfully!\n")
            break

def view_students(students):
    if not students:
        print("No students available.\n")
        return
    for s in students:
        print(f"{s['name']} ({s['section']}) - Spanish: {s['spanish']}, English: {s['english']}, Social: {s['social']}, Science: {s['science']} - Average: {s['average']:.2f}")
    print()

def view_top_students(students):
    if not students:
        print("No students available.\n")
        return
    top = sorted(students, key=lambda x: x["average"], reverse=True)[:3]
    for s in top:
        print(f"{s['name']} ({s['section']}) - Average: {s['average']:.2f}")
    print()

def view_global_average(students):
    if not students:
        print("No students available.\n")
        return
    avg = sum(s["average"] for s in students) / len(students)
    print(f"Global average: {avg:.2f}\n")

def delete_student(students):
    name = input("Enter student name to delete: ").strip()
    section = input("Enter student section: ").strip()
    for s in students:
        if s["name"] == name and s["section"] == section:
            confirm = input(f"Are you sure you want to delete {name} ({section})? (y/n): ")
            if confirm.lower() == "y":
                students.remove(s)
                print("\nStudent deleted successfully.\n")
            return
    print("Student not found.\n")

def view_failed_students(students):
    failed = []
    for s in students:
        subjects_failed = {subj: s[subj] for subj in ["spanish","english","social","science"] if s[subj] < 60}
        if subjects_failed:
            failed.append((s["name"], s["section"], subjects_failed))
    if not failed:
        print("No failed students.\n")
    else:
        for name, section, subjects in failed:
            print(f"{name} ({section}) failed in: {subjects}")
        print()
