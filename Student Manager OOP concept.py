class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def display(self):
        print(f"Name: {self.name} | Age: {self.age} | Course: {self.course}")


class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self):
        name = input("Enter name: ")
        try:
            age = int(input("Enter age: "))
        except ValueError:
            print("❌ Age must be a number!")
            return
        course = input("Enter course: ")

        student = Student(name, age, course)
        self.students.append(student)
        print("✅ Student added!")

    def view_students(self):
        if not self.students:
            print("No students yet.")
            return

        print("\n📌 Student List:")
        for s in self.students:
            s.display()

    def search_student(self):
        keyword = input("Enter name to search: ").lower()
        found = False

        for s in self.students:
            if keyword in s.name.lower():
                s.display()
                found = True

        if not found:
            print("❌ Student not found.")

    def menu(self):
        while True:
            print("\n--- Student Manager ---")
            print("1. Add Student")
            print("2. View Students")
            print("3. Search Student")
            print("4. Exit")

            choice = input("Choose: ")

            if choice == "1":
                self.add_student()
            elif choice == "2":
                self.view_students()
            elif choice == "3":
                self.search_student()
            elif choice == "4":
                print("Bye 👋")
                break
            else:
                print("❌ Invalid choice!")


manager = StudentManager()
manager.menu()
