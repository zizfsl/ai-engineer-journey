class Student:

    #class attributes
    school_name = "ABC University"  
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def __repr__(self):
        return f"Student('{self.name}', {self.age}, {self.score})"

    def __str__(self):
        return f"{self.name} ({self.age}) - Score: {self.score}"


    def introduce(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old. My score is {self.score}.")
    
    def is_passed(self):
        return self.score >= 60
    
    def update_score(self, new_score):
        self.score = new_score

student1 = Student("Alice", 20, 85)
student1.update_score(95)
student1.introduce()
vl= student1.school_name
print(vl)
print(student1.is_passed())


student1.introduce()
print(student1.is_passed())

stuent2 = Student("Bob", 22, 90)
stuent2.introduce()

Student.school_name = "XYZ University"
print(student1.school_name)

student1.school_name = "PQR University"
print(student1.school_name)
print(stuent2.school_name)


#-------------------str-------------------
print(student1)  # Output: <__main__.Student object at 0x7f8b8c8d9e50>

#-------------------exercises-------------------

class Course:
    def __init__(self, name, students=None):
        self.name = name
        self.students = students if students is not None else []

    def    add_student(self, student):
        self.students.append(student)   
    
    def average_score(self):
        if not self.students:
            return 0
        total = sum(student.score for student in self.students)
        return total / len(self.students)
    
    def top_student(self):
        if not self.students:
            return None
        return max(self.students, key=lambda student: student.score)
    
course = Course("Math")

course.add_student(student1)
course.add_student(stuent2)
print(course.average_score())  # Output: 92.5
print(course.top_student())  # Output: Student('Bob', 22, 90)   

