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
            df_unicos = unicos.get_df()

        except:
            raise 'Error'
            
        print('\n df_unicos')
        print(df_unicos)
            
        return df_unicos
    
    def crea_grupos(self):
        """
        Muestra el DataFrame con los valores únicos del DataFrame de la base de datos y los muestra
        el el QTableView del diálogo.
        """
        
        df_unicos = self.get_dataframe_unicos()
            
        # Salida Pyqt5.
        self.v.salida_grupos(df_unicos)


class CntGruposDialogo:
    """Controlador de los grupos."""
    
    def __init__(self, dialogo):
        """
        Crea la ventana de Dialogo.
        """
        
        self.d = dialogo
        
    def acepta_cambios(self):
        
        table = TableModelData(self.d.model)
        self.d.df_grupos = table.get_df_model_data()
        
        return self.d.df_grupos
        
        
        # # https://stackoverflow.com/questions/21280061/get-data-from-every-cell-from-a-qtableview
        # data = []
        
        # for row in range(self.d.model.rowCount()):
        #     data.append([])
        #     for column in range(self.d.model.columnCount()):
        #         index = self.d.model.index(row, column)
        #         # We suppose data are strings
        #         # data[row].append(str(self.d.model.data(index).toString()))
        #         data[row].append(str(self.d.model.data(index)))
        
        # for col in range(self.d.model.columnCount()):
        #     data.append([])
            
        #     for row in range(self.d.model.rowCount()):
        #         index = self.d.model.index(row, col)
        #         data[col].append(self.d.model.data(index))
        
        
        
        # print('\n data')
        # print(data)
        
        
        
        
        
        # df_unicos = CntGrupos.get_dataframe_unicos(self)
        # df_grupos = df_unicos.copy()
        
        # print('\n df_unicos 2')
        # print(df_unicos)
        
        # print('\n df_grupos')
        # print(df_grupos)
        
    
        



