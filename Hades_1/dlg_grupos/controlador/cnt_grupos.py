# -*- coding: utf-8 -*-
"""
Controlador de los grupos

Created on Wed Sep 10 14:55 2020

__author__ = Pedro Biel
__version__ = 0.0.0
__email__ = structural.eng.biel@gmail.com
"""


from dlg_grupos.datos.datos_grupos import Unicos
from dlg_grupos.modelo.mdl_tablemodeleditable import PandasModelEditable


class CntGrupos:
    """Controlador de los grupos."""
    
    def __init__(self, ventana):
        """Crea la ventana de MainWindow."""
        
        self.v = ventana
    
    def crea_grupos(self):
        """
        Crea el DataFrame df_grupos con los valores únicos del DataFrame 
        df_db y asigna dichos valores a un modelo.
        Muestra el modelo en el diálogo de grupos.
        """
        
        # Status bar.
        text = 'Creando grupos.'
        self.v.status_bar(text)
        
        # Asigna valores de df_db a df_grupos y de df_grupos al modelo.
        # print('\nCntGrupos.crea_grupos.df_grupos')
        # print(self.v.df_grupos)
        # print('\nCntGrupos.crea_grupos.df_relaciones')
        # print(self.v.df_relaciones)
        if self.v.df_grupos.empty:  # Si es la primera vez que se llama a los grupos.
            self.v.df_grupos = self.get_grupos()
        
        try:
            self.v.df_grupos_prev = self.v.df_grupos.copy()
            # print('\nCntGrupos.crea_grupos.df_grupos_prev')
            # print(self.v.df_grupos_prev)
        except AttributeError as e:
            print('AttributeError en CntGrupos.crea_grupos():', e)
            
        model = self.get_modelo(self.v.df_grupos)
        
        # Salida en el diálogo.
        self.v.call_dialogo_grupos(self.v.df_grupos, model)
        
        # Status bar.
        text = 'Grupos creados.'
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
            print('Exception en CntGrupos.dataframe_unicos():', e)
            
        return df_unicos
    
    def get_grupos(self):
        """Getter del DataFrame con los grupos únicos."""
        
        try:
            df_unicos = self.dataframe_unicos()
            
            return df_unicos
        
        except UnboundLocalError as e:
            print('UnboundLocalError en CntGrupos.get_grupos():', e)

    
    def get_modelo(self, df):
        """Getter del modelo con los datos del DataFrame."""
        
        model = PandasModelEditable(df)
        
        return model


# class CntGruposDialogo:
#     """Controlador de los grupos."""
    
#     def __init__(self, dialogo):
#         """
#         Crea la ventana de Dialogo.
#         """
        
#         self.d = dialogo
        
#     def tablemodel_df(self):
#         """Transfiere los datos de QTableModel a pandas DataFrame."""
        
#         table = TableModelData(self.d.model)
#         # self.d.df_grupos = table.get_df_model_data()
        
#         # return self.d.df_grupos
    