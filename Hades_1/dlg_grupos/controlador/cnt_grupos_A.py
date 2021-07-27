# -*- coding: utf-8 -*-
"""
Controlador de los grupos

Created on Wed Sep 10 14:55 2020

__author__ = Pedro Biel
__version__ = 0.0.0
__email__ = structural.eng.biel@gmail.com
"""


import pandas as pd

from dlg_grupos.datos.datos_grupos import Unicos


class CntGrupos:
    """Controlador de los grupos."""
    
    def __init__(self, ventana):
        """
        Crea la ventana de MainWindow/Dialog.
        """
        
        self.v = ventana
        
        # Librerías.
        self.pd = pd
        
        self.df_unicos = pd.DataFrame()
    
    def get_dataframe_unicos(self):
        """
        Sea df_db el DataFrame de la base de datos obtiene un nuevo DataFrame 
        con los valores únicos del DataFrame de la base de datos.
        """
        
        # print('self.btn_grupos.clicked.connect(self.cnt_grupos.crea_grupos)')
        # print('\n df_db')
        # print(self.v.df_db)
    
        try:
            unicos = Unicos(self.v.pd, self.v.df_db)
            self.df_unicos = unicos.get_df()

        except:
            raise 'Error'
            
        print('\n df_unicos')
        print(self.df_unicos)
            
        return self.df_unicos
        
    
    def crea_grupos(self):
        """
        Muestra el DataFrame con los valores únicos del DataFrame de la base de datos y los muestra
        el el QTableView del diálogo.
        """
        
        df_unicos = self.get_dataframe_unicos()
            
        # Salida Pyqt5.
        self.v.salida_grupos(df_unicos)
        
    def acepta_cambios(self):
        
        # df_unicos = self.get_dataframe_unicos()
        self.v.df_grupos = self.df_unicos.copy()
        
        print('\n df_unicos 2')
        print(self.df_unicos)
        
        print('\n df_grupos')
        print(self.v.df_grupos)
        
    
        



