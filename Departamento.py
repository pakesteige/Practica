__author__ = 'francisco'


class Departamento:
    """
        Modela un departamento

        :author: Francisco Lopez Baena
        :version: 1
    """

    def __init__(self, nombre_depto, id_depto):
        """
        descripcion breve: constructor

        descripcion detallada: inicializador de la clase departamento

        :param nombre_depto: nombre del departamento. Le pasamos el nombre por la variable nombre_depto
        :param id_depto: identificador del departamento. Le pasamos el identificador por la variable id_depto
        :return: no devuelve nada
        """
        self.nombre_depto = nombre_depto
        self.id_depto = id_depto
        self.lista_emp = []

    def aniadir_emp(self, Empleado):
        """

        :param Empleado: empleados de un departamento
        :return: no devuelve nada
        """
        self.lista_emp.append(Empleado)


    def get_salario_total(self):
        """
        descripcion breve: obtener salario

        descripcion detallada: metodo para obtener el salario total de todos los empleados del departamento

        :return: total
        """
        total = 0
        for i in self.lista_emp:
            total += i.get_salario()
        return total

    def get_nombre_depto(self):
        """
        descripcion breve: nombre departmaneto

        descripcion detallada: metodo para obtener el nombre del departamento

        :return: nombre_depto
        """
        return self.nombre_depto

    def get_salario_total_mensual(self):
        """
        descripcion breve: salario total mensual

        descripcion detallada: metodo para obtener el salario total mensual de los empleados del departamento

        :return: total
        """
        total = 0
        for i in self.lista_emp:
            total += i.get_salario_mensual()
        return total