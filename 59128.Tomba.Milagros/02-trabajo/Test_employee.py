import unittest
from Employee import Person
from Employee import Employee

class Test_person(unittest.TestCase):
    def test_get_person(self):
        persona1 = Person("Milagros", 19, "Tomba", 2615080491).get_person()
        self.assertEqual(persona1, (["Milagros", 19, "Tomba", 2615080491]))
    
class  Test_employee(unittest.TestCase):
    def test_get_employee(self):
        employee1 = Employee("Milagros", 19, 30000, "Tomba", 2615080491).get_employee()
        self.assertEqual(employee1, (["Milagros", 19, 30000, "Tomba", 2615080491]))

    def Test_pay_tax_pay(self):
        taxes = Employee("Milagros", 19, 40000,"Tomba", 2615080491).pay_tax()
        self.assertEqual(taxes, "Paga impuestos")

    def Test_pay_tax_no_pay(self):
        taxes2 = Employee("Milagros", 19, 30000,"Tomba", 2615080491).pay_tax()
        self.assertEqual(taxes2, "No paga impuestos")
    
       

if __name__ == '__main__':
  unittest.main()
 