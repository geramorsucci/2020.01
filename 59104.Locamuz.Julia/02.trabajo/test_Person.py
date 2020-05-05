import unittest
from employee import Person
from parameterized import parameterized


class TestPerson(unittest.TestCase):
    @parameterized.expand([
        ('Julia', 20),
        ('Rosario', 26),
        ('Diego', 56)
    ])
    def test_get_person(self, name, age):
        persona = Person(name, age)
        datosPersona = persona.get_person()
        self.assertEqual(datosPersona, [name, age])


if __name__ == '__main__':
    unittest.main()
