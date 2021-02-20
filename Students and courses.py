class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    
    def get_grade(self):
        return self.grade

class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []
    
    def add_student(self,student_instance):
        if len(self.students) < self.max_students:
            self.students.append(student_instance)
            return True
        return False
    
    def get_average_grade(self):
        if len(self.students) == 0:
            return 0
        value = 0
        for student in self.students:
            value += student.get_grade()
        return value/len(self.students)

if __name__ == "__main__":
    s1 = Student("S",20,100)
    s2 = Student("Tim",19,75)
    s3 = Student("Jill",19,50)
    print(s1.get_grade())

    course = Course("Science",2)
    print(course.add_student(s1))
    print(course.add_student(s2))
    print(course.add_student(s3))

    print(course.students[1].name)

    print("average grade",course.get_average_grade())
