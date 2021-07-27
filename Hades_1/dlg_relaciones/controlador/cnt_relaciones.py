# -*- coding: utf-8 -*-
"""
Controlador de las relaciones

Created on Fri Oct 2 12:57 2020

__author__ = Pedro Biel
__version__ = 0.0.0
__email__ = structural.eng.biel@gmail.com
"""


from dlg_relaciones.datos.datos_relaciones import Unicos
from dlg_relaciones.modelo.mdl_tablemodeleditable import PandasModelEditable


class CntRelaciones:
    """Controlador de las relaciones."""
    
    def __init__(self, ventana):
        """Crea la ventana de MainWindow."""
        
        self.v = ventana
        
    def crea_relaciones(self):
        """
        Crea el df_relaciones con los grupos únicos del DataFrame df_grupos y
        asigna dichos valores a un modelo.
        Muestra el modelo en el diálogo de relaciones.
        """
        
        # Status bar.
        text = 'Creando relaciones, coeficientes de mayoración y redondeos.'
        self.v.status_bar(text)
    
        # Asigna valores de df_grupos a df_relaciones y de df_relaciones al modelo.
        # print('\nCntRelaciones.crea_relaciones.df_grupos_prev')
        # print(self.v.df_grupos_prev)
        # print('\nCntRelaciones.crea_relaciones.df_grupos')
        # print(self.v.df_grupos)
        # print('\nCntRelaciones.crea_relaciones.df_relaciones')
        # print(self.v.df_relaciones)
        equals = self.compara_dataframes_grupos()
        
        if equals:  # Los DataFrames son iguales, self.v.df_relaciones no se modifica.
            
            if self.v.df_relaciones.empty:  # Si es la primera vez que se llama a las relaciones.
                self.v.df_relaciones = self.get_relaciones()
                
        else:  # Los DataFrames no son iguales, self.v.df_relaciones se modifica.
            self.v.df_relaciones = self.get_relaciones()
            # Se hace una nueva copia de df_grupos para que la próxima vez que 
            # se llame a las relaciones sean iguales df_grupos y df_grupos_prev
            # y se conserven los cambios en relaciones.
            self.v.df_grupos_prev = self.v.df_grupos.copy()

        # Convierte columna Relación en mayusculas.
        self.v.df_relaciones = self.df_str_upper(
            self.v.df_relaciones, 'Relación'
            )
        
        model = self.get_modelo(self.v.df_relaciones)
        
        # Salida en el diálogo.
        self.v.call_dialogo_relaciones(self.v.df_relaciones, model)
    
        #  Status bar.
        text = 'Relaciones, coeficientes de mayoración y redondeos creados.'
        self.v.status_bar(text)
        
    def compara_dataframes_grupos(self):
        """
        Compara el DataFrame Grupos con el DataFrame previo.
        Si son iguales retorna True, si no lo son, retorna False.
        """

        equals = self.v.df_grupos.equals(self.v.df_grupos_prev)
        # print('\nequals:', equals)
        
        return equals
    
    def dataframe_relaciones(self):
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
    
    def get_relaciones(self):
        """Getter del DataFrame con las relaciones."""
        
        df_relaciones = self.dataframe_relaciones()
        # print('\nCntRelaciones.get_relaciones.df_relaciones')
        # print(df_relaciones)
            
        return df_relaciones
    
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
