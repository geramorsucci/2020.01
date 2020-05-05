import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):
    def test_employee(self):
        person1 = Employee("Agustin", 19, 40000)
        self.assertEqual(Employee.get_employee(person1), ["Agustin", 19, 40000])

    def test_pay_tax_pay(self):
        person1 = Employee("Agustin", 19, 40000)
        self.assertEqual(Employee.pay_tax(person1), 'Paga impuestos')

    def test_pay_tax_no_pay(self):
        person1 = Employee("Agustin", 19, 20000)
        self.assertEqual(Employee.pay_tax(person1), 'No paga impuestos')


if __name__ == '__main__':
    unittest.main()
