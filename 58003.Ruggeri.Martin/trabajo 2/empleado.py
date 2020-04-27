import unittest
from persona import Person, Employee
from parameterized import parameterized


class TestPerson(unittest.TestCase):
  @parameterized.expand([("martin", 21, ["martin", 21]),
                          ("juan", 30, ["juan", 30])])
  def test_get_person(self,name, age, string):
    person = Person(name, age).get_person()
    self.assertEqual(person, string) 


if __name__ == "__main__":
    unittest.main()


class TestEmployee(unittest.TestCase):
  @parameterized.expand([("martin", 21, 2500, ["martin", 21, 2500], "no paga impuestos"),
                          ("juan", 30, 3500, ["juan", 30, 3500], "Paga impuestos")])
  def test_get_employee(self,name, age, salary, string, str_impuestos):
    employee = Employee(name, age, salary).get_employee()
    self.assertEqual(employee, string) 
    impuestos = Employee(name, age, salary).pay_tax()
    self.assertEqual(impuestos, str_impuestos) 

if __name__ == "__main__":
    unittest.main()

