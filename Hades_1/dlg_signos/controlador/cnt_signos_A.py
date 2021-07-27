# -*- coding: utf-8 -*-
"""
Controlador de los signos de las cargas

Created on Wed Oct 21 12:23 2020

__author__ = Pedro Biel
__version__ = 0.0.0
__email__ = pbiel@taimweser.com
"""


from dlg_signos.datos.datos_signos import Signos
from dlg_signos.modelo.mdl_tablemodeleditable import PandasModelEditable


class CntSignos:
    """Controlador de los signos de las cargas."""
    
    def __init__(self, ventana):
        """Crea la ventana de MainWindow."""
        
        self.v = ventana
        
    def crea_signos(self):
        """
        Crea el df_signos con las direcciones de las cargas y asigna dichos 
        valores a un modelo.
        Muestra el modelo en el diálogo de grupos.
        """
        
        # Status bar.
        text = 'Creando signos de las cargas.'
        self.v.status_bar(text)
        
        # Asigna valores de df_db a df_ruedas y de df_ruedas al modelo.
        if self.v.df_signos.empty:  # Si es la primera vez que se llama a las ruedas.
            self.v.df_signos = self.get_signos()
        
        try:
            self.v.df_signos_prev = self.v.df_signos.copy()
            # print('\nCntSignos.crea_signos.df_signos_prev')
            # print(self.v.df_signos_prev)
        except AttributeError as e:
            print('AttributeError en CntSignos.crea_signos():', e)
            
        model = self.get_modelo(self.v.df_signos)
        
        # Salida en el diálogo.
        self.v.call_dialogo_signos(self.v.df_signos, model)
        
        # Status bar.
        text = 'Signos de las cargas creados.'
        self.v.status_bar(text)
        
    def dataframe(self):
        """Obtiene un nuevo DataFrame con los signos."""

        signos = Signos(self.v.pd)
        df = signos.get_df()
        
        return df
    
    def get_signos(self):
        """Getter del DataFrame con los signos de las cargas."""
        
        try:
            df = self.dataframe()
            
            return df
        
        except UnboundLocalError as e:
            print('UnboundLocalError en CntSignos.get_signos():', e)

    
    def get_modelo(self, df):
        """Getter del modelo con los datos del DataFrame."""
        
        model = PandasModelEditable(df)
        
        return model
