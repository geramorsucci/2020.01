import unittest
from parameterized import parameterized
from employee import Employee
from administration import Administration

class TestAdmin (unittest.TestCase):
    @parameterized.expand([
        {
    0: {'name': 'Claudio', 'surname': 'Pico', 'age': 30, 'phone': 155858585,'salary':30000}, 
    1: {'name': 'NIcolas', 'surname': 'Pico', 'age': 30, 'phone': 155858585,'salary':20000}
    }

    ])

    def test_add_employee(self, name, surname, age, phone, salary, legajo, result):
        employee = Employee(name, surname, age, phone, salary)
        employeelist = Administration().add_employee(employee)
        self.assertEqual(employee, result)


if __name__ == "__main__":
    unittest.main()
