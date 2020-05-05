import unittest
from persona import Person, Empleado

class TestPerson(unittest.TestCase):

    def test_get_person(self):
        persona = Person("Mariano",21)
        self.assertEqual([persona.nombre, persona.edad], Person.get_persona(persona))

class TestEmployee(unittest.TestCase):

    def test_get_empleado(self):
        empleado = Empleado("Mariano", 21, 3500)
        self.assertEqual([empleado.nombre, empleado.edad, empleado.salario], Empleado.get_empleado(empleado))

class TestPagaImpuesto(unittest.TestCase):

    def test_paga_impuesto(self):
        empleado2 = Empleado("Mariano", 21, 3500)
        self.assertEqual("Paga impuestos", Empleado.paga_impuesto(empleado2))

class TestNoPagaImpuesto(unittest.TestCase):

    def test_no_paga_impuesto(self):
        emp3 = Empleado("Mariano", 21, 2300)
        self.assertEqual("No paga impuestos", Empleado.paga_impuesto(emp3))

if __name__ == "__main__":
    unittest.main()
