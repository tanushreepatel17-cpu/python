#class variable = shared among all instances of a class
#                  defined outside the cosntructor allow you to share data among all objects created from that class.
# 
   #defining a class

class Student: #class variable

    class_year = 2025
    num_students = 0 #count number of students created from this class

    def __init__ (self, name,age):   #when you create an instance of the inner class, __init__ stores name and age on that instance
        self.name = name
        self.age = age
        Student.num_students += 1
student1 = Student("Spongebob", 30)
student2 = Student("tanushree", 20)
student3 = Student("mahima",45)

print(f"my graduating class of {Student.class_year} has {Student.num_students} students")

print(student1.name, student1.age, student1.class_year)
print(student2.name, student2.age, student2.class_year)
print(student3.name, student3.age, student3.class_year)