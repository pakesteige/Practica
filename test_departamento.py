from unittest import TestCase
from mockito import *
from Departamento import *
from Empleado import *

__author__ = 'francisco'


class TestDepartamento(TestCase):
    def test_get_salario_total(self):
        empleado1=mock(Empleado)
        when(empleado1).get_salario().thenReturn(200)

        empleado2=mock(Empleado)
        when(empleado2).get_salario().thenReturn(100)

        empleado3=mock(Empleado)
        when(empleado3).get_salario().thenReturn(300)

        departamento = Departamento('Trianon',1)
        departamento.aniadir_emp(empleado1)
        departamento.aniadir_emp(empleado2)
        departamento.aniadir_emp(empleado3)

        self.assertEqual(departamento.get_salario_total(),600)

    def test_get_salario_total_mensual(self):
        empleado1=mock(Empleado)
        when(empleado1).get_salario_mensual().thenReturn(200)

        empleado2=mock(Empleado)
        when(empleado2).get_salario_mensual().thenReturn(100)

        empleado3=mock(Empleado)
        when(empleado3).get_salario_mensual().thenReturn(300)

        departamento = Departamento('Trianon',2)
        departamento.aniadir_emp(empleado1)
        departamento.aniadir_emp(empleado2)
        departamento.aniadir_emp(empleado3)

        self.assertEqual(departamento.get_salario_total_mensual(),600)