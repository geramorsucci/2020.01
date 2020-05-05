class Person():

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def get_persona(self):
        return [self.nombre, self.edad]

class Empleado (Person):

    def __init__(self, nombre, edad, salario):
        Person.__init__(self, nombre, edad)
        self.salario = salario

    def get_empleado(self):
        return [self.nombre, self.edad, self.salario]

    def paga_impuesto(self):
        if self.edad < 32 and self.salario > 3000:
            return "Paga impuestos"
        else:
            return "No paga impuestos"

"""
prueba