import unittest
from classes import Employee, Person
 @parameterized.expand([
        ("Oriel", "Barroso", 23, 155000000, 25000, 0, {"name": "Oriel", "surname": "Barroso", "age": 23, "phone": 155000000, "salary":25000, "legajo": 0 })
    ])

class test_classes(unittest.TestCase):
    def test_get_employee(self):
        
        emp1 = Employee.get_employee(self)
        self.assertEqual(emp1, ["Oriel", 23, 32000])

    def test_pay_taxes(self):
        self.age = 48
        self.salary = 50000
        imp1 = Employee.pay_tax(self)
        self.assertEqual(imp1, "No paga impuestos")

    def test_no_pay_taxes(self):
        self.age = 23
        self.salary = 31999
        imp2 = Employee.pay_tax(self)
        self.assertEqual(imp2, "Paga impuestos")


if __name__ == "__main__":
    unittest.main()
