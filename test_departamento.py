from unittest import TestCase
from mockito import *
from Departamento import *

__author__ = 'francisco'


class TestDepartamento(TestCase):
    def test_get_salario_total(self):
        empleado1=mock()
        when(empleado1).get_salario().thenReturn(200)

        empleado2=mock()
        when(empleado2).get_salario().thenReturn(100)

        empleado3=mock()
        when(empleado3).get_salario().thenReturn(300)

        departamento = Departamento('hp',2)
        departamento.aniadir_emp(empleado1)
        departamento.aniadir_emp(empleado2)
        departamento.aniadir_emp(empleado3)

        self.assertEqual(departamento.get_salario_total(),600)