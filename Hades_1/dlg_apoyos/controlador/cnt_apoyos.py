# -*- coding: utf-8 -*-
"""
Controlador de los apoyos

Created on Fri Oct 2 12:57 2020

__author__ = Pedro Biel
__version__ = 0.0.0
__email__ = structural.eng.biel@gmail.com
"""


from dlg_apoyos.datos.datos_apoyos import Unicos
from dlg_apoyos.modelo.mdl_tablemodeleditable import PandasModelEditable


class CntApoyos:
    """Controlador de los apoyos."""
    
    def __init__(self, ventana):
        """Crea la ventana de MainWindow."""
        
        self.v = ventana
        
    def crea_apoyos(self):
        """
        Crea el DataFrame df_apoyos con los valores únicos del DataFrame 
        df_db y asigna dichos valores a un modelo.
        Muestra el modelo en el diálogo de relaciones.
        """
        
        # Status bar.
        text = 'Creando apoyos.'
        self.v.status_bar(text)
    
        # Asigna valores de df_db a df_apoyos y de df_apoyos al modelo.
        if self.v.df_apoyos.empty:  # Si es la primera vez que se llama a los apoyos.
            self.v.df_apoyos = self.get_apoyos()
                
        try:
            self.v.df_apoyos_prev = self.v.df_apoyos.copy()
            # print('\nCntApoyos.crea_apoyos.df_apoyos_prev')
            # print(self.v.df_apoyos_prev)
        except AttributeError as e:
            print('AttributeError en CntApoyos.crea_apoyos():', e)

        # Convierte columna Apoyos en mayusculas.
        self.v.df_apoyos = self.df_str_upper(
            self.v.df_apoyos, 'Apoyo'
            )
        
        model = self.get_modelo(self.v.df_apoyos)
        
        # Salida en el diálogo.
        self.v.call_dialogo_apoyos(self.v.df_apoyos, model)
    
        #  Status bar.
        text = 'Apoyos creados.'
        self.v.status_bar(text)
    
    def dataframe_unicos(self):
        """
        Sea df_db el DataFrame de la base de datos obtiene un nuevo DataFrame 
        con los valores únicos del DataFrame de la base de datos.
        """
        
        try:
            unicos = Unicos(self.v.pd, self.v.df_db)
            df_unicos = unicos.get_df()
        except Exception as e:
            print('Exception en CntApoyos.dataframe_unicos():', e)
            
        return df_unicos
    
    def get_apoyos(self):
        """Getter del DataFrame con los apoyos únicos."""
        
        try:
            df_unicos = self.dataframe_unicos()
            
            return df_unicos
        
        except UnboundLocalError as e:
            print('UnboundLocalError en CntApoyos.get_apoyos():', e)
    
    def get_modelo(self, df):
        """Getter del modelo con los datos del DataFrame."""
        
        model = PandasModelEditable(df)
        
        return model
    
    def df_str_upper(self, df, col):
        """
        Convierte la columna 'col' del DataFrame en strings mayúsculas.
        """
        df_upper = df.copy()
        df_upper[col] = df[col].str.upper()
        
        return df_upper
