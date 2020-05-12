import unittest
from classes import Person
from parameterized import parameterized


class test_classes(unittest.TestCase):
    @parameterized.expand([
        ("Oriel", "Barroso", 23, 156250112, {"name" : "Oriel", "surname": "Barroso", "age" : 23, "cellphone" : 156250112})
    ])
    def test_get_person(self, name, surname, age, cellphone, result):
        person = Person(name, surname, age, cellphone)
        persona1 = person.get_person()
        self.assertEqual(persona1, result)


if __name__ == "__main__":
    unittest.main()
