import csv, os

FIELDS = ["name", "section", "spanish", "english", "social", "science", "average"]

def export_data(students):
    if not students:
        print("No data to export.\n")
        return
    with open("students.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        writer.writeheader()
        for s in students:
            # asegurar que las claves estén en minúscula
            row = {
                "name": s["name"],
                "section": s["section"],
                "spanish": float(s["spanish"]),
                "english": float(s["english"]),
                "social": float(s["social"]),
                "science": float(s["science"]),
                "average": float(s["average"])
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
            student = {
                "name": row["name"],
                "section": row["section"],
                "spanish": float(row["spanish"]),
                "english": float(row["english"]),
                "social": float(row["social"]),
                "science": float(row["science"]),
                "average": float(row["average"])
            }
            students.append(student)
    print("Data imported.\n")
