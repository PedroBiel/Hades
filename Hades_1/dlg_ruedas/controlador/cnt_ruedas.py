# -*- coding: utf-8 -*-
"""
Controlador del nº de ruedas

Created on Wed Oct 21 09:40:14 2020

__author__ = Pedro Biel
__version__ = 0.0.0
__email__ = pbiel@taimweser.com
"""


from dlg_ruedas.datos.datos_ruedas import Unicos
from dlg_ruedas.modelo.mdl_tablemodeleditable import PandasModelEditable


class CntRuedas:
    """Controlador del nº de ruedas."""
    
    def __init__(self, ventana):
        """Crea la ventana de MainWindow."""
        
        self.v = ventana
        
    def crea_ruedas(self):
        """
        Crea el df_ruedas con los nudos únicos del DataFrame df_apoyos y 
        asigna dichos valores a un modelo.
        Muestra el modelo en el diálogo de grupos.
        """
        
        # Status bar.
        text = 'Creando nº de ruedas.'
        self.v.status_bar(text)
        
        # Asigna valores de df_apoyos a df_ruedas y de df_ruedas al modelo.
        equals = self.compara_dataframes_apoyos()
        
        if equals:  # Los DataFrames son iguales, self.v.df_ruedas no se modifica.
        
            if self.v.df_ruedas.empty:  # Si es la primera vez que se llama a las ruedas.
                self.v.df_ruedas = self.get_ruedas()
        
        else:  # Los DataFrames no son iguales, self.v.df_ruedas se modifica.
            self.v.df_ruedas = self.get_ruedas()
            # Se hace una nueva copia de df_apoyos para que la próxima vez que 
            # se llame a las ruedas sean iguales df_apoyos y df_apoyos_prev
            # y se conserven los cambios en ruedas.
            self.v.df_apoyos_prev = self.v.df_apoyos.copy()
            
        model = self.get_modelo(self.v.df_ruedas)
        
        # Salida en el diálogo.
        self.v.call_dialogo_ruedas(self.v.df_ruedas, model)
        
        # Status bar.
        text = 'Nº de ruedas creadas.'
        self.v.status_bar(text)
        
    def compara_dataframes_apoyos(self):
        """
        Compara el DataFrame Apoyos con el DataFrame previo.
        Si son iguales retorna True, si no lo son, retorna False.
        """

        equals = self.v.df_apoyos.equals(self.v.df_apoyos_prev)
        # print('\nequals:', equals)
        
        return equals
    
    def dataframe_ruedas(self):
        """
        Sea df_apoyos el DataFrame con los apoyos obtiene un nuevo DataFrame 
        con los valores únicos del DataFrame de los apoyos.
        """
    
        try:
            unicos = Unicos(self.v.pd, self.v.df_apoyos)
            df_unicos = unicos.get_df()
        except Exception as e:
            print('Exception en CntRuedas.dataframe_ruedas():', e)
        
        return df_unicos
    
    def get_ruedas(self):
        """Getter del DataFrame con las ruedas."""
        
        df_ruedas = self.dataframe_ruedas()
            
        return df_ruedas
    
    def get_modelo(self, df):
        """Getter del modelo con los datos del DataFrame."""
        
        model = PandasModelEditable(df)
        
        return model
