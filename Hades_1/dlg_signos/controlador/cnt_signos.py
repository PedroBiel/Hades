# -*- coding: utf-8 -*-
"""
Controlador de los signos de las cargas

Created on Wed Oct 21 12:23 2020

__author__ = Pedro Biel
__version__ = 0.0.0
__email__ = pbiel@taimweser.com
"""


from dlg_signos.datos.datos_signos import Unicos
from dlg_signos.modelo.mdl_tablemodeleditable import PandasModelEditable


class CntSignos:
    """Controlador de los signos de las cargas."""
    
    def __init__(self, ventana):
        """Crea la ventana de MainWindow."""
        
        self.v = ventana
        
    def crea_signos(self):
        """
        Crea el df_signos de las direcciones de las cargas con los grupos 
        únicos y asigna dichos valores a un modelo.
        Muestra el modelo en el diálogo de signos.
        """
        
        # Status bar.
        text = 'Creando signos de las cargas.'
        self.v.status_bar(text)
        
        # Asigna valores de df_grupos a df_signos y de df_signos al modelo.
        equals = self.compara_dataframes_grupos()
        
        if equals:  # Los DataFrames son iguales, self.v.df_signos no se modifica.
            
            if self.v.df_signos.empty:  # Si es la primera vez que se llama a los signos.
                self.v.df_signos = self.get_signos()
                
        else:  # Los DataFrames no son iguales, self.v.df_signos se modifica.
            self.v.df_signos = self.get_signos()
            # Se hace una nueva copia de df_grupos para que la próxima vez que 
            # se llame a los signos sean iguales df_grupos y df_grupos_prev
            # y se conserven los cambios en signos.
            self.v.df_grupos_prev = self.v.df_grupos.copy()
            
        model = self.get_modelo(self.v.df_signos)
        
        # Salida en el diálogo.
        self.v.call_dialogo_signos(self.v.df_signos, model)
        
        # Status bar.
        text = 'Signos de las cargas creados.'
        self.v.status_bar(text)
        
    def compara_dataframes_grupos(self):
        """
        Compara el DataFrame Grupos con el DataFrame previo.
        Si son iguales retorna True, si no lo son, retorna False.
        """
        
        equals = self.v.df_grupos.equals(self.v.df_grupos_prev)
        # print('\nequals:', equals)
   
        return equals       
        
    def dataframe_signos(self):
        """
        Sea df_grupos el DataFrame con los grupos obtiene un nuevo DataFrame 
        con los valores únicos del DataFrame de los grupos.
        """
    
        try:
            unicos = Unicos(self.v.pd, self.v.df_grupos)
            df_unicos = unicos.get_df()
        except Exception as e:
            print('Exception en CntRelaciones.dataframe_relaciones():', e)
        
        return df_unicos
    
    def get_signos(self):
        """Getter del DataFrame con los signos de las cargas."""
        
        df_signos = self.dataframe_signos()
            
        return df_signos

    def get_modelo(self, df):
        """Getter del modelo con los datos del DataFrame."""
        
        model = PandasModelEditable(df)
        
        return model
