import random
class Employee():
    instances = []

    def __init__(self,name):
        self.name = name
        self.email = name +'@gmail.com'
        __class__.instances.append(self)

    emp_1 = Employee('akshay')  
    emp_2 = Employee('akshay40')
    emp_3 = Employee('harish')
    emp_4 = Employee('poki')
    emp_5 = Employee('heybro')

    randIndex = random.randrange(len(Employee.instances))
    rand = Employee.instances[randIndex]

    print(rand.name + " " + rand.email)
