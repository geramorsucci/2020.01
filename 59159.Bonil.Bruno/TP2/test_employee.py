import unittest
import employee
from employee import Employee

class TestEmployee(unittest.TestCase):
    def test_get_employee(self):
        empleado = Employee("Bruno", 19, 5000)
        datos_empleado = empleado.get_employee()
        self.assertEqual(datos_empleado, ["Bruno", 19, 5000])

    def test_pay_tax_pay(self):
        empleado1 = Employee("Lucas", 25, 70000)
        salario = empleado1.pay_tax()
        self.assertEqual(salario, "Paga impuestos")

    def test_pay_tax_no_pay(self):
        empleado2 = Employee("Juan", 35, 2000)
        salario = empleado2.pay_tax()
        self.assertEqual(salario, "No paga impuestos")


if __name__ == '__main__':
    unittest.main()