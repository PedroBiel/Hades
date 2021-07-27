# -*- coding: utf-8 -*-
"""
Controlador de los grupos

Created on Wed Sep 10 14:55 2020

__author__ = Pedro Biel
__version__ = 0.0.0
__email__ = structural.eng.biel@gmail.com
"""


from dlg_grupos.datos.datos_grupos import Unicos
from dlg_grupos.datos.datos_modelo import TableModelData


class CntGrupos:
    """Controlador de los grupos."""
    
    def __init__(self, ventana):
        """
        Crea la ventana de MainWindow.
        """
        
        self.v = ventana
    
    def dataframe_unicos(self):
        """
        Sea df_db el DataFrame de la base de datos obtiene un nuevo DataFrame 
        con los valores únicos del DataFrame de la base de datos.
        """
        
        try:
            unicos = Unicos(self.v.pd, self.v.df_db)
            df_unicos = unicos.get_df()

        except:
            raise 'Error'
            
        return df_unicos
    
    def get_grupos_unicos(self):
        """Getter del DataFrame con los grupos únicos."""
        
        df_unicos = self.dataframe_unicos()
            
        return df_unicos


class CntGruposDialogo:
    """Controlador de los grupos."""
    
    def __init__(self, dialogo):
        """
        Crea la ventana de Dialogo.
        """
        
        self.d = dialogo
        
    def tablemodel_df(self):
        """Transfiere los datos de QTableModel a pandas DataFrame."""
        
        table = TableModelData(self.d.model)
        self.d.df_grupos = table.get_df_model_data()
        
        return self.d.df_grupos
    