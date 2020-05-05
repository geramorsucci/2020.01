import unittest
from employee import Employee
from parameterized import parameterized


class TestEmployee(unittest.TestCase):
    @parameterized.expand([
        ('Julia', 20),
        ('Rosario', 26),
        ('Diego', 56)
    ])
    def test_get_employee(self, name, age, salary):
        empleado = Employee(name, age, salary)
        datosEmpleado = empleado.get_employee()
        self.assertEqual(datosEmpleado, [name, age, salary])

    @parameterized.expand([
         ('Julia', 20),
         ('Rosario', 26),
         ('Diego', 56)
    ])
    def test_tax_pay(self, name, age, salary):
        empleado = Employee(name, age, salary)
        salarioEmpleado = empleado.pay_tax()
        self.assertEqual(salarioEmpleado, "Paga impuestos")

    @parameterized.expand([
         ('Julia', 20),
         ('Rosario', 26),
         ('Diego', 56)
    ])
    def test_tax_no_pay(self, name, age, salary):
        empleado = Employee(name, age, salary)
        salarioEmpleado = empleado.pay_tax()
        self.assertEqual(salarioEmpleado, "No paga impuestos")


if __name__ == '__main__':
    unittest.main()
