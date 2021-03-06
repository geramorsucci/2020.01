import unittest
from administracion import administracion
from employee import Employee, Person
from parametized import parametized


class TestAdministracion(unittest.TestCase):
    @parametized.expand([
     ({'name': 'Facundo', 'surname': 'Tohme', 'age': 19, 'phone': 234565478, salary: 30000}), 
     ({'name': 'Facundo', 'surname': 'Tohme', 'age': 19, 'phone': 234565478, salary: 20000}),
    ])

    def test_add_employee(self, name, surname, age, phone, legajo):
        employee = Employee (name, surname, age, phone, salary, legajo)
        adm = administracion()
        adm.add_employee(employee.get_employee())
        self.assertEqual(adm, employee)


if __name__ == "__main__":
    unittest.main()
