class Person:

    def __init__(self, name=None , surname=None, age=None, key=None):
        self.name = name
        self.surname = surname
        self.age = age
        self.key = key

    def agregarPersona(self):
        print("\n Agreganddo persona")
        self.name = str(input("\nIngrese el nombre: "))
        self.surname = str(input("Ingrese el apellido: "))
        self.age = str(input("Ingrese la edad: "))
        self.key = int(input("Ingrese la clave que quiere asignarle: "))

    def updatearPersona(self, resultado=False):
        print("\nActualizando persona")
        if resultado == False:
            self.key = int(input("\nIngrese la clave de la persona que quiere modificar: "))
        elif resultado == True:
            self.name = str(input("Ingrese el nombre: "))
            self.surname = str(input("Ingrese el apellido: "))
            self.age = str(input("Ingrese la edad: "))
    
    def eliminarPersona(self, resultado=False):
        self.key = int(input("\nIngrese la clave de la persona que quiere eliminar: "))
            


