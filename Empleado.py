__author__ = 'francisco'


class Empleado:
    """
    Modela un empleado

    :author: Francisco Lopez Baena
    :version: 1
    """

    def __init__(self, nombre, apellidos, dni, direccion, edad, salario, email):
        """
        descripcion breve: constructor

        descripcion detallada: inicializador de la clase empleado

        :param nombre: nombre del empleado
        :param apellidos: apellidos del empleado
        :param dni: dni del empleado
        :param direccion: direccion del empleado
        :param edad: edad del empleado
        :param salario: salario del empleado
        :param email: correo electronico del empleado
        :return: no devuelve nada
        """
        self.nombre = nombre
        self.apellidos = apellidos
        self.dni = dni
        self.direccion = direccion
        self.edad = edad
        self.salario = salario
        self.email = email

    def get_salario(self):
        """

        :return: salario
        """
        return self.salario

    def get_dni(self):
        """
        descripcion breve: dni del empleado

        descripcion detallada: metodo para obtener el dni del empleado

        :return: dni
        """
        return self.dni

    def get_nombre_apellidos(self):
        """
        descripcion breve: nombre completo del empleado

        descripcion detallada: metodo para obtener el nombre completo del empleado

        :return: string
        """
        return self.nombre + " " + self.apellidos

    def get_edad(self):
        """
        descripcion breve: edad del empleado

        descripcion detallada: metodo para obtener la edad del empleado

        :return: edad
        """
        return self.edad

    def get_email(self):
        """
        descripcion breve: email del empleado

        descripcion detallada: metodo para obtener el correo electronido del empleado

        :return: email
        """
        return self.email

    def get_direccion(self):
        """
        descripcion breve: direccion del empleado

        descripcion detallada: metodo para obtener la direccion del empleado

        :return: direccion
        """
        return self.direccion

    def get_salario_mensual(self):
        """
        descripcion breve: salario al mes del empleado

        descripcion detallada: metodo para obtener el salario al mes del empleado

        :return: salario mensual
        """
        return self.get_salario() / 12

