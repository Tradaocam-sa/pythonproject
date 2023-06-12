class Person:
    def __init__ (self, name, birth):
        self.name = name
        self.birth = birth
    
    def get_person(self):
        return f'Name: {self.name}, Birth: {self.birth} '
    

class Dancer(Person):
    def __init__ (self,name, birth,  style):
        Person.__init__(self, name, birth) 
        self.style = style

    def get__style(self):
        return f'Style: {self.style}'

    def describe(self):
        print("I'm the best dancer")


class Student(Dancer):
    # def __init__ (self, name, birth, style):
    #     # Person.__init__(self, name, birth)
    #     Dancer.__init__(self,name, birth, style)

    def get__student(self):      
        return f"Name: {self.name}, Birth: {self.birth}, Style: {self.style}"
    
    # def describe(self):
    #     print("wtf")


if __name__ == '__main__':
    name = input("Enter name: ")
    birth = input("Enter birth: ")
    style = input("Enter style: ")
    student = Student(name, birth, style)
    print(student.get__student())
    student.describe()
    student.get_person()

    
