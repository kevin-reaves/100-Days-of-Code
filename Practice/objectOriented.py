class Employee:
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print("Total Employees ", Employee.empCount)

    def displayEmployee(self):
        print("Name: ", self.name, " Salary: ", self.salary)

#emp1 = Employee("Kevin", 100000)
#emp1.displayCount()
#emp1.displayEmployee()

#emp1.salary = 50000
#emp1.displayEmployee()
#del emp1


#print(Employee.__doc__)
#print(Employee.__name__)
#print(Employee.__module__)
#print(Employee.__bases__)
#print(Employee.__dict__)


####################################################

class Parent:
    parentAttr = 100
    def __init(self):
        print("Calling parent constructor")

    def parentMethod(self):
        print("Calling parent method")

    def setAttr(self, attr):
        Parent.parentAttr = attr

    def getAttr(self):
        print("Attribute ", Parent.parentAttr)

class Child(Parent):
    def __init__(self):
        print("Calling child constructor")

    def childMethod(self):
        print('Calling child method')

#c = Child()
#c.childMethod()
#c.parentMethod()
#c.setAttr(200)
#c.getAttr()

