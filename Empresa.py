__author__ = 'francisco'


class Empresa:
    """
        Modela una empresa
        :author: Francisco Lopez Baena
        :version: 1
    """
    def __init__(self, nombre_empresa, cif, razon_social):
        """
        descripcion breve: constructor

        descripcion detallada: inicializador de la clase empresa

        :param nombre_empresa: nombre de la empresa
        :param cif: cif de la empresa
        :param razon_social: razon social de la empresa
        :param lista_dep: lista de departamentos de la empresa
        :return: no devuelve nada
        """
        self.nombre_empresa = nombre_empresa
        self.cif = cif
        self.razon_social = razon_social
        self.lista_dep = []

