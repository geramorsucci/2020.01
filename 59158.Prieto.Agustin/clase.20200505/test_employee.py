import unittest
from employee import Employee
from parameterized import parameterized


class TestEmployee(unittest.TestCase):
    @parameterized.expand([
        ('Agustin', 'Prieto', 19, 2616804596, 25000,  {'name': 'Agustin',
        'surname': 'Prieto', 'age': 19,
        'cellphone': 2616804596, 'salary': 25000})


    ])
    def test_employee(self, name, surname, age, cellphone, salary, result):
        person1 = Employee(name, surname, age, cellphone, salary)

        self.assertEqual(person1.get_employee(), result)

    @parameterized.expand([
        ('Agustin', 30000, 19, "Paga impuestos")


    ])
    def test_pay_tax_pay(self, name, salary, age, result):
        person1 = Employee(name, salary, age)
        self.assertEqual(person1.pay_tax(), result)

    @parameterized.expand([
        ('Agustin', 40, 10000, 'No paga impuestos')

    ])
    def test_pay_tax_not_pay(self, name, age, salary, result):
        person1 = Employee(name, age, salary)
        self.assertEqual(person1.pay_tax(), result)


if __name__ == '__main__':
    unittest.main()
