# -*- coding: utf-8 -*-
"""
Controlador de coeficientes

Created on Wed Oct 28 14:49 2020

__author__ = Pedro Biel
__version__ = 0.0.0
__email__ = pbiel@taimweser.com
"""


from dlg_coeficientes.datos.datos_coeficientes import Unicos
from dlg_coeficientes.modelo.mdl_tablemodeleditable import PandasModelEditable


class CntCoeficientes:
    """Controlador de los coeficientes de mayoración y del redondeo."""
    
    def __init__(self, ventana):
        """Crea la ventana de MainWindow."""
        
        self.v = ventana
        
    def crea_coeficientes(self):
        """
        Crea el df_coeficientes con los nudos únicos del DataFrame df_apoyos y 
        asigna dichos valores a un modelo.
        Muestra el modelo en el diálogo de grupos.
        """
        
        # Status bar.
        text = 'Creando los coeficientes de mayoración y de redondeo.'
        self.v.status_bar(text)
        
        # Asigna valores de df_apoyos a df_coeficientes y de df_coeficientes al modelo.
        equals = self.compara_dataframes_apoyos()
        
        if equals:  # Los DataFrames son iguales, self.v.df_coeficientess no se modifica.
        
            if self.v.df_coeficientes.empty:  # Si es la primera vez que se llama a los coeficientes.
                self.v.df_coeficientes = self.get_coeficientes()
        
        else:  # Los DataFrames no son iguales, self.v.df_coeficientes se modifica.
            self.v.df_coeficientes = self.get_coeficientes()
            # Se hace una nueva copia de df_apoyos para que la próxima vez que 
            # se llame a las ruedas sean iguales df_apoyos y df_apoyos_prev
            # y se conserven los cambios en coeficientes.
            self.v.df_apoyos_prev = self.v.df_apoyos.copy()
            
        model = self.get_modelo(self.v.df_coeficientes)
        
        # Salida en el diálogo.
        self.v.call_dialogo_coeficientes(self.v.df_coeficientes, model)
        
        # Status bar.
        text = 'Coeficientes de mayoración y de redondeo creados.'
        self.v.status_bar(text)
        
    def compara_dataframes_apoyos(self):
        """
        Compara el DataFrame Apoyos con el DataFrame previo.
        Si son iguales retorna True, si no lo son, retorna False.
        """
        
        equals = self.v.df_apoyos.equals(self.v.df_apoyos_prev)
        # print('\nequals:', equals)
        
        return equals
    
    def dataframe_coeficientes(self):
        """
        Sea df_apoyos el DataFrame con los apoyos obtiene un nuevo DataFrame 
        con los valores únicos del DataFrame de los apoyos.
        """
    
        try:
            unicos = Unicos(self.v.pd, self.v.df_grupos)
            df_unicos = unicos.get_df()
        except Exception as e:
            print('Exception en CntCoeficientes.dataframe_coeficientes():', e)
        
        return df_unicos
    
    def get_coeficientes(self):
        """Getter del DataFrame con las ruedas."""
        
        df_coeficientes = self.dataframe_coeficientes()
            
        return df_coeficientes

    def get_modelo(self, df):
        """Getter del modelo con los datos del DataFrame."""
        
        model = PandasModelEditable(df)
        
        return model
