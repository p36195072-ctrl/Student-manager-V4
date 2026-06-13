students = {}

while True:

    print("\n===== STUDENT MANAGER =====\n")
    print("1. Add Student")
    print("2. Search Student")
    print("3. View All Students")
    print("4. Show All Students")
    print("5. Delete Student")
    print("6. Exit")
    print("Total students:", len(students))

    choice = input("Enter choice: ")

    if choice == "1":
        try:
            name = input("Enter name: ").strip()
            if name == "":
                print("Name can't be empty")
                continue

            age = input("Enter age: ").strip()
            if age == "":
                print("Age can't be empty")
                continue

            city = input("Enter city: ").strip()
            if city == "":
                print("City can't be empty")
                continue

            student_class = input("Enter class: ").strip()
            if student_class == "":
                print("Student class can't be empty")
                continue

            student_class = int(student_class)

            students[name] = {
                "age": age,
                "city": city,
                "class": student_class
            }

            print("Student Added!")

        except ValueError:
            print("Invalid class number")

    elif choice == "2":
        name = input("Search student: ").strip()

        if name == "":
            print("Name in search can't be empty.")
            continue

        if name in students:
            print(students[name])
        else:
            print("Student Not Found")

    elif choice == "3":
        if len(students) == 0:
            print("No students found")
        
        else:
            for name, details in students.items():
                print(name, ":", details)

    elif choice == "4":
        if len(students) == 0:
            print("No Students Found")
        else:
            for name, details in students.items():
                print(name, ":", details)

    elif choice == "5":
        name = input("Enter student name: ").strip()
        if name == "":
            print ("You have to enter name to delete")
            continue

        if name in students:
            del students[name]
            print("Deleted Successfully")
        else:
            print("Student Not Found")

    elif choice == "6":
        print("Exiting...")
        break

    else:
        print("Invalid Choice")