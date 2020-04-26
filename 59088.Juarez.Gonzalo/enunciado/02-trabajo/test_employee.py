import unittest
from employee import Person, Employee

class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.personTest = Person("Gonzalo", 19)
        self.employeeTestArr = [Employee("Gonzalo", 19, 20000), Employee("X", 22, 35000)]

    def tearDown(self):
        self.personaTest = Person("Gonzalo", 19)
        self.employeeTestArr = [Employee("Gonzalo", 19, 20000), Employee("X", 22, 35000)]

    def test_get_person(self):
        self.assertListEqual(self.personTest.get_person(), ["Gonzalo", 19])

    def test_get_employee(self):
        self.assertListEqual(self.employeeTestArr[0].get_employee(), ["Gonzalo", 19, 20000])

    def test_pay_taxes(self):
        self.assertEqual(self.employeeTestArr[1].pay_tax(), "Paga impuestos")

    def test_no_pay_taxes(self):
        self.assertEqual(self.employeeTestArr[0].pay_tax(), "No paga impuestos")

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestEmployee)
    unittest.TextTestRunner().run(suite)