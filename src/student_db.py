import json
import os

DATABASE_FILE = "Student.json"

# 1. Datenbank laden oder neu erstellen
if os.path.exists(DATABASE_FILE):
    with open(DATABASE_FILE, "r") as f:
        database = json.load(f)
        print("Existing database loaded successfully!")
else:
    database = {}  # <-- Geschweifte Klammern für ein Dictionary!
    print("No existing database found. Created a new empty database.")


# 2. Funktion definieren (Gehört außerhalb der Schleife nach oben)
def create_student(name, age, grade):
    student_dict = {
        "name": str(name),
        "age": int(age),
        "grade": int(grade)
    }
    return student_dict


# 3. Haupt-Schleife
while True:
    print("\nHello Iam CLIP the Client Persistent Student Database")
    print("[1] Add Student")
    print("[2] View All")
    print("[3] Quit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        Name = input("Please enter the Student name: ")
        age = input("What is your age? ")
        grade = input("What is your grade? ")

        # Diese Zeilen MÜSSEN eingerückt im 'if'-Block liegen,
        # sonst wird die 'if-elif'-Kette unterbrochen!
        my_student = create_student(Name, age, grade)
        database[Name] = my_student
        print(f"Added {Name} to local database.")

    elif choice == 2:
        print("\n==========================================")
        print("            STUDENT DATABASE              ")
        print("==========================================")

        # Falls die Datenbank komplett leer ist
        if not database:
            print("No students registered yet.")
        else:
            # Wir gehen jeden Schüler in unserer Datenbank nacheinander durch
            for student_id, info in database.items():
                # Der Trick mit :<12 reserviert genau 12 Zeichen Platz für den Namen,
                # damit die Spalten sauber untereinander ausgerichtet sind!
                print(f"Name: {student_id:<12} | Age: {info['age']:<3} | Grade: {info['grade']}")

        print("==========================================")

    elif choice == 3:
        # Speichern beim Verlassen
        with open("Student.json", "w") as f:
            json.dump(database, f, indent=4)
        print("Database saved successfully. Goodbye!")
        break  # Schleife beenden