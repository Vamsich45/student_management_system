class Student:
    def __init__(self, name, roll_num, marks):
        self.name = name
        self.roll_num = roll_num
        self.marks = marks  

    def total(self):
        return sum(self.marks)

    def percentage(self):
        if len(self.marks) == 0:
            return 0
        return self.total() / len(self.marks)

    def is_pass(self):
        return self.percentage() >= 40


class StudentSystem:
    def __init__(self):
        self.students = []

    def add_student(self, name, roll_num, marks):
        student = Student(name, roll_num, marks)
        self.students.append(student)
        print("Student added successfully!")

    def view_students(self):
        if not self.students:
            print("No students found")
            return

        for s in self.students:
            print("\n-------------------")
            print("Name:", s.name)
            print("Roll:", s.roll_num)
            print("Marks:", s.marks)
            print("Total:", s.total())
            print("Percentage:", s.percentage())

            if s.is_pass():
                print("Result:", "Pass")
            else:
                print("Result:", "Fail")

    def search_student(self, roll_num):
        for s in self.students:
            if s.roll_num == roll_num:
                print("\nStudent Found:")
                print("Name:", s.name)
                print("Roll:", s.roll_num)
                print("Marks:", s.marks)
                print("Percentage:", s.percentage())

                if s.is_pass():
                    print("Result:", "Pass")
                else:
                    print("Result:", "Fail")
                return

        print("Student not found")


# --------------------------------

system = StudentSystem()

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        name = input("Enter name: ")
        roll_num = int(input("Enter roll: "))
        marks = list(map(int, input("Enter marks separated by space: ").split()))
        system.add_student(name, roll_num, marks)

    elif choice == 2:
        system.view_students()

    elif choice == 3:
        roll_num = int(input("Enter roll number: "))
        system.search_student(roll_num)

    elif choice == 4:
        print("Exiting...")
        break

    else:
        print("Invalid choice")
