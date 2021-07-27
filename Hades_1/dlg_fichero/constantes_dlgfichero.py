# -*- coding: utf-8 -*-
"""
HADES
Constantes para el diálogo de fichero

Created on Mon Jul 27 14:01:31 2020

__author__ = Pedro Biel
__version__ = 0.0.0
__email__ = pbiel@taimweser.com
"""


class Constantes:
    """Valores constantes para el diálogo de fichero."""
    
    def __init__(self):
        """Crea constantes ABRIR_DATOS y TIPO_FICHEROS."""
    
        self.__ABRIR_DATOS = 'Abrir datos'
        self.__TIPO_FICHEROS = 'Tipo de ficheros (*.db)'
        self.__GUARDAR_EXCEL = 'Guardar hoja Excel'
        self.__TIPO_FICHEROS_XLSX = 'Tipo de ficheros (*.xlsx)'
        self.__GUARDAR_DATOS = 'Guardar datos de implantaciones'
    
    def get_abrir_datos(self):
        """Getter de ABRIR_DATOS."""
        
        return self.__ABRIR_DATOS
    
    def get_tipo_ficheros(self):
        """Getter de TIPO_FICHEROS."""
        
        return self.__TIPO_FICHEROS
    
    def get_guardar_excel(self):
        """Getter de GUARDAR_EXCEL."""
        
        return self.__GUARDAR_EXCEL
    
    def get_tipo_ficheros_excel(self):
        """Getter de TIPO_FICHEROS_XLSX."""
        
        return self.__TIPO_FICHEROS_XLSX
    
    def get_guardar_datos(self):
        """Getter de GUARDAR_DATOS."""
        
        return self.__GUARDAR_DATOS
