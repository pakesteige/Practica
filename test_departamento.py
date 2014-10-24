from unittest import TestCase
from mockito import *
from Departamento import *
from Empleado import *

__author__ = 'francisco'


class TestDepartamento(TestCase):

    def test_get_salario_total(self):
        empleado1=mock()
        when(empleado1).get_salario().thenReturn(12000)

        empleado2=mock()
        when(empleado2).get_salario().thenReturn(13000)

        empleado3=mock()
        when(empleado3).get_salario().thenReturn(16000)

        departamento = Departamento('trianon',1)
        departamento.aniadir_emp(empleado1)
        departamento.aniadir_emp(empleado2)
        departamento.aniadir_emp(empleado3)

        self.assertEqual(departamento.get_salario_total(),41000)

    def test_get_salario_total_mensual(self):
        empleado1=mock(Empleado)
        when(empleado1).get_salario_mensual().thenReturn(1000)

        empleado2=mock(Empleado)
        when(empleado2).get_salario_mensual().thenReturn(1100)

        empleado3=mock(Empleado)
        when(empleado3).get_salario_mensual().thenReturn(1200)


        departamento = Departamento('Trianon2',2)
        departamento.aniadir_emp(empleado1)
        departamento.aniadir_emp(empleado2)
        departamento.aniadir_emp(empleado3)

        self.assertEqual(departamento.get_salario_total_mensual(),3300)
