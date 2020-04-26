import unittest
from employee import Person , Employee

class TestPerson(unittest.TestCase):
    
   def test_get_person(self):
       self.name = "Ivan"
       self.age  = 20
       listaDatos = Person.get_person(self)
       self.assertEqual(listaDatos,['Ivan', 20])

class TestEmployee(unittest.TestCase):

    def test_get_employee(self):
        self.salary = 4000
        self.name = "Ivan"
        self.age = 20
        listaDatos2 = Employee.get_employee(self)
        self.assertEqual(listaDatos2,["Ivan", 20, 4000])
    
    def test_tax_pay(self):
        self.salary = 4000
        self.age = 20
        self.name = "Ivan"
        listaDatos3 = Employee.pay_tax(self)
        self.assertEqual(listaDatos3, "Paga impuestos")

    def test_tax_no_pay(self):
        self.salary = 2000
        self.age = 20
        self.name = "Nahuel"
        listaDatos4 = Employee.pay_tax(self)
        self.assertEqual(listaDatos4, "No paga impuestos")

if __name__ == "__main__":
    unittest.main()
