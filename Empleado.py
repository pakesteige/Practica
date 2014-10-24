__author__ = 'francisco'

class Empleado:
    def __init__(self,nombre,apellidos,dni,direccion,edad,salario):
        self.nombre=nombre
        self.apellidos=apellidos
        self.dni=dni
        self.direccion=direccion
        self.edad=edad
        self.salario

    def get_salario(self):
        return self.salario

    def get_dni(self):
        return self.dni

    def get_nombre_apellidos(self):
        return self.nombre + " " + self.apellidos