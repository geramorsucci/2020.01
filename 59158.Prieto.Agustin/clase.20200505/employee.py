
class Person:
    
    def __init__(self, name, surname, age, cellphone):
        self.name = name
        self.age = age
        self.surname = surname
        self.age = age
        self.cellphone = cellphone
        
    def get_person(self):
        return self.__dict__
 
 
class Employee(Person):
    
    def __init__(self, name, surname, age, cellphone=0, salary=0):
        Person.__init__(self, name, surname, age, cellphone)
        self.salary = salary

    def get_employee(self):
        return self.__dict__
        
    # declaramos el metodo paga_impuestos
    # comprobara si el empleado debe pagar o no
    # return "Paga impuestos" or "No paga impuestos"

    def pay_tax(self):
        if self.salary < 30000 and self.age > 32:
            return "No paga impuestos"
        else:
            return "Paga impuestos"
 