import unittest
from person import Person, Employee

class TestPerson(unittest.TestCase):
    def test_get_person(self):
        self.name = "Federico"
        self.surname = "Calderon"
        self.age = 20 
        self.phone = 1234
        person = Person.get_person(self)
        self.assertEqual(person,{'name ':self.name,'surname ':self.surname,'age ':self.age,'phone ':self.phone})

class TestEmployee(unittest.TestCase):

    def test_get_employee(self):    
        self.name = "Federico"
        self.surname = "Calderon"
        self.age = 20
        self.phone = 1234
        self.salary = 3000
        employee = Employee.get_employee(self)
        self.assertEqual(employee,{'name ':self.name,'surname ':self.surname,'age ':self.age,'phone ':self.phone, "salary ":self.salary})

    def test_get_pay_tax(self):
        self.name = 'Federico'
        self.surname = 'Calderon'
        self.age = 20
        self.phone = 1234
        self.salary = 4500
        t = Employee.get_pay_tax(self)
        self.assertEqual(t,'Paga impuestos')

    def test_get_no_pay_tax(self):
        self.name = 'Federico'
        self.surname = 'Calderon'
        self.age = 20
        self.phone = 1234213
        self.salary = 2500
        t = Employee.get_pay_tax(self)
        self.assertEqual(t,'No paga impuestos')

if __name__ == "__main__":
    unittest.main()
