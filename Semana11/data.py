import csv
import os
from student import Student

FIELDS = ["name", "section", "spanish", "english", "social", "science", "average"]

def export_data(students):
    if not students:
        print("No data to export.\n")
        return

    with open("students.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        writer.writeheader()

        for s in students:
            row = {
                "name": s.name,
                "section": s.section,
                "spanish": s.spanish,
                "english": s.english,
                "social": s.social,
                "science": s.science,
                "average": s.average
            }
            writer.writerow(row)

    print("Data exported.\n")

def import_data(students):
    if not os.path.exists("students.csv"):
        print("No CSV file found.\n")
        return

    with open("students.csv", "r") as f:
        reader = csv.DictReader(f)
        students.clear()

        for row in reader:
            student = Student(
                row["name"],
                row["section"],
                float(row["spanish"]),
                float(row["english"]),
                float(row["social"]),
                float(row["science"])
            )
            students.append(student)

    print("Data imported.\n")