from repository import Repository
# from person import Person


class PersonService:

    def get_personList(self):
        return Repository.person

    def find_by_name(self, name):
        name = name.upper()
        for i in self.get_personList():
            if self.get_personList()[i].name == name:
                return self.get_personList()[i]
        return False

    # Agrega una persona en el dicionario person, definido en Repository
    def add_person(self, person):
        Repository.person[len(Repository.person)] = person

    # Actualiza datos de una person del diccionario person
    # key clave diccionario
    # object Person
    def update_person(self, key, person):
        Repository.person[key] = person

    # Elimina persona segun key del dic person
    def delete_person(self, key):
        del Repository.person[key]
