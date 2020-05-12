from person import Person
from personService import PersonService


def print_personlist():
    for i in personService.get_personList():
        print(personService.get_personList()[i].__dict__)


if __name__ == '__main__':

    personService = PersonService()

    # Agregamos una persona
    p1 = Person('federico', 'gonzales', '20')
    personService.add_person(p1)

    # Agregamos una persona
    p1 = Person('claudio', 'pico', '33')
    personService.add_person(p1)

    # Agregamos al hermano **********************
    p2 = Person("nicolas", "pico", '40')
    print("===ADD NICOLAS===")
    personService.add_person(p2)

    print_personlist()
    # {
    #   0: {'_name': 'FEDERICO', '_surname': 'GONZALEZ',
    #       '_age': '20'},
    #   1: {'_name': 'NICOLAS', '_surname': 'PICO',
    #       '_age': 30},
    #   2: {'_name': 'NICOLAS', '_surname': 'PICO',
    #       '_age': 30}
    # }
    # Update Federico
    print("===UPDATE FEDERICO===")
    personService.find_by_name("federico").age = 30
    print_personlist()

    # delete person
    personService.delete_person(2)
    print("===DELETE NICOLAS===")
    print_personlist()

    # {
    #   0: {'_name': 'FEDERICO', '_surname': 'GONZALEZ',
    #       '_age': '20'},
    #   1: {'_name': 'NICOLAS', '_surname': 'NICOLAS',
    #       '_age': 41}
    # }
