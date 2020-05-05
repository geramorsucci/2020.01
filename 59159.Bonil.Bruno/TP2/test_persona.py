import unittest
import employee
from employee import Person

class TestPersona(unittest.TestCase):
    def test_get_person(self):
        persona = Person("Bruno", 19)
        datos_persona = persona.get_person()
        self.assertEqual(datos_persona, ["Bruno", 19])



if __name__ == '__main__':
    unittest.main()