import unittest
from employee import Person, Employee


class PersonTest (unittest.TestCase):

    def test_get_person(self):
        self.name = "Gerardo"
        self.surname = "Morsucci"
        self.age = 19
        self.phone = 2615755151

        person = Person.get_person(self)
        self.assertEqual(person, {'name': 'Gerardo', 'surname': 'Morsucci', 'age': 19, 'phone': 2615755151})


class EmployeeTest (unittest.TestCase):
    def test_get_employee(self):
        self.name = "Gerardo"
        self.surname = "Morsucci"
        self.age = 19
        self.phone = 2615755151
        self.salary = 30001
        employee = Employee.get_employee(self)
        self.assertEqual(employee, {'name': 'Gerardo', 'surname': 'Morsucci', 'age': 19, 'phone': 2615755151, 'salary': 30001})

    def test_pay_tax_pay(self):
        self.salary = 40000
        self.age = 22
        taxes = Employee.pay_tax(self)
        self.assertEqual(taxes, "Paga impuestos")

    def test_pay_tax_no_pay(self):
        self.salary = 20000
        self.age = 19
        taxes = Employee.pay_tax(self)
        self.assertEqual(taxes, "No paga impuestos")


if __name__ == "__main__":
    unittest.main()
