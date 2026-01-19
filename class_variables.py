# class variables = Sharead among all instances of a class
#                   Defined outside the constructor
#                   Allow you to share data among all objects created from that class

class Student: 

    class_year = 2024   # class variable accessible to all objects 
    num_students = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_students += 1    # each time we initialize an object the num_student will increase by 1

student1 = Student("Spongebob", 30)
student2 = Student("Patrick", 35)
print(Student.num_students) # will return 2 since we have two students
student3 = Student("Squidward", 55)
print(Student.num_students) # wil return 3 now

print(student1.class_year)  # it is advised to access through the class name directly
print(Student.class_year)   # you can access a class variable from the class itself