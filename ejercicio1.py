# -*- coding: utf-8 -*-# -*-
# Programa: Servicio de Estacionamiento
# Objetivo: llevar un orden de las horas que el vehiculo estuvo estacionado 
#           mostrar un reporte del cobro.
# Autor: Saudy Zavala
# Fecha: 13/marzo/2020

class Menu:
    """
    Mostrara un menu de opciones a seleccionar

    """
def __init__(self):
        self.Datos = datos()
 def display_menu(self):
        """ Despliega el menú principal """
        print("""
             Menú principal

            1. Número de placa del vehículo
            2. Marca
            3. Modelo
            4. Tipo de vehículo (automóvil o motocicleta)
            5. Hora de ingreso.
            6. Estado (true por defecto).
             """)


