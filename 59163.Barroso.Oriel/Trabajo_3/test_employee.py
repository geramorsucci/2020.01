from class1 import Person, Employee
import administration
from parameterized import parameterized
import unittest


class test_classes(unittest.TestCase):
    @parameterized.expand([
                            ("Oriel", "Barroso", 23, 155000000, 25000, 0, {"name": "Oriel", "surname": "Barroso", "age": 23, "phone": 155000000, "salary":25000, "legajo": 0 }),
                            ("Nicolas", "Barroso", 32, 155000001, 32000, 1, {'name':"Nicolas",'surname':"Barroso",'age':32,'phone':155000001, "salary": 32000, "legajo":1})
                        ])
    def test_add_employee(self, name, surname, age, phone, salary, legajo, result):
        employee = Employee(name, surname, age, phone, salary, legajo)
        emp1 = employee.get_employee()
        self.assertEqual(emp1, result)


if __name__ == "__main__":
    unittest.main()
    