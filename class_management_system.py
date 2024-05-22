class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.courses = []

    def enroll(self, course):
        self.courses.append(course)

    def __str__(self):
        courses = ', '.join([course.name for course in self.courses])
        return f'Student ID: {self.student_id}, Name: {self.name}, Courses: {courses}'

class Course:
    def __init__(self, course_id, name):
        self.course_id = course_id
        self.name = name

    def __str__(self):
        return f'Course ID: {self.course_id}, Name: {self.name}'

class ClassManagementSystem:
    def __init__(self):
        self.students = {}
        self.courses = {}

    def add_student(self, student_id, name):
        if student_id in self.students:
            print("Student ID already exists.")
        else:
            student = Student(student_id, name)
            self.students[student_id] = student
            print("Student added successfully.")

    def add_course(self, course_id, name):
        if course_id in self.courses:
            print("Course ID already exists.")
        else:
            course = Course(course_id, name)
            self.courses[course_id] = course
            print("Course added successfully.")

    def enroll_student_in_course(self, student_id, course_id):
        if student_id not in self.students:
            print("Student ID not found.")
        elif course_id not in self.courses:
            print("Course ID not found.")
        else:
            student = self.students[student_id]
            course = self.courses[course_id]
            student.enroll(course)
            print("Student enrolled in course successfully.")

    def display_students(self):
        for student in self.students.values():
            print(student)

    def display_courses(self):
        for course in self.courses.values():
            print(course)

if __name__ == "__main__":
    cms = ClassManagementSystem()
    while True:
        print("\nClass Management System")
        print("1. Add Student")
        print("2. Add Course")
        print("3. Enroll Student in Course")
        print("4. Display Students")
        print("5. Display Courses")
        print("6. Exit")
        choice = input("Enter choice: ").strip()

        if choice == '1':
            student_id = input("Enter student ID: ").strip()
            name = input("Enter student name: ").strip()
            cms.add_student(student_id, name)
        elif choice == '2':
            course_id = input("Enter course ID: ").strip()
            name = input("Enter course name: ").strip()
            cms.add_course(course_id, name)
        elif choice == '3':
            student_id = input("Enter student ID: ").strip()
            course_id = input("Enter course ID: ").strip()
            cms.enroll_student_in_course(student_id, course_id)
        elif choice == '4':
            cms.display_students()
        elif choice == '5':
            cms.display_courses()
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")





# # Explanation:
# Student Class:

# Attributes: student_id, name, courses.
# Methods: enroll to add courses to the student, __str__ to return a string representation of the student.
# Course Class:

# Attributes: course_id, name.
# Methods: __str__ to return a string representation of the course.
# ClassManagementSystem Class:

# Attributes: students (a dictionary of students), courses (a dictionary of courses).
# Methods:
# add_student: Adds a student to the system.
# add_course: Adds a course to the system.
# enroll_student_in_course: Enrolls a student in a course.
# display_students: Displays all students.
# display_courses: Displays all courses.
# Main Program Loop:

# Provides a menu to add students, add courses, enroll students in courses, display students, display courses, and exit the program.

