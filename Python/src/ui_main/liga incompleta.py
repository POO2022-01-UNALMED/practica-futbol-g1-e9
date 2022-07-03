'''
@File    :   servicio_pagado_exception.py
@Time    :   2022/01/31
@Author  :   Erik Gonzalez
@Version :   1.0
@Desc    :   El error ocurre cuando se intenta cobrar el servicio otra vez
'''

from .view_exception import ViewException

class generarcalendarioException(ViewException):
    def __init__(self, message="La cantidad de Equipos de la liga aun no esta completa, porfavor revise el numero de equipos"):
        super().__init__(message)
