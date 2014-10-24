__author__ = 'francisco'

class Departamento:
    def __init__(self,nombre_depto,id_depto):
        self.nombre_depto=nombre_depto
        self.id_depto=id_depto
        self.lista_emp=[]

    def aniadir_emp(self,Empleado):
        self.lista_emp.append(Empleado)

    def get_salario_total(self):
        total=0
        for i in self.lista_emp:
            total+=i.get_salario()
        return total