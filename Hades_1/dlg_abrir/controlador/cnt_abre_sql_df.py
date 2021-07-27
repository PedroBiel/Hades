 # -*- coding: utf-8 -*-
"""
HADES
Controlador de abrir datos de SQLite y pasarlos a pandas DataFrame

Created on Wen Feb 24 7:31 2021

__author__ = Pedro Biel
__version__ = 1.0.1
__email__ = structural.eng.biel@gmail.com

Versión 1.0.1: Desactiva la opción de abrir de SQL la tabla 'Implantaciones'
para importar únicamente la configuración de las implantaciones y mantener
los datos importados previamente en la applicación.
"""


from pyqt5_clases.qfiledialog import FileDialog

from transferenciadatos.sqlitepandasdf import SQLitePandasDF

from dlg_fichero.constantes_dlgfichero import Constantes


class CntAbreSQLDF:
    """Controlador de abrir datos de SQLite y pasarlos a pandas DataFrame."""
    
    def __init__(self, ventana):
        self.v = ventana
        
    def get_sqlite3(self):
        """Getter de la librería sqlite3."""
        
        return self.v.sqlite3
    
    def set_dictionary_proyecto(self, df):
        """Setter del DataFrame Proyecto."""
        
        df_proyecto = df.copy()
        d = df_proyecto.to_dict('records')[0]
        self.v.d_proyecto = d
        
    def set_dataframe_implantaciones(self, df):
        """Setter del DataFrame Implantaciones."""
        
        self.v.df_implantaciones = df.copy()
        
    def set_dataframe_grupos(self, df):
        """Setter del DataFrame Grupos."""
        
        self.v.df_grupos = df.copy()
        
    def set_dataframe_relaciones(self, df):
        """Setter del DataFrame Relaciones."""
        
        self.v.df_relaciones = df.copy()
        
    def set_dataframe_apoyos(self, df):
        """Setter del DataFrame Apoyos."""
        
        self.v.df_apoyos = df.copy()
        
    def set_dataframe_ruedas(self, df):
        """Setter del DataFrame Ruedas."""
        
        self.v.df_ruedas = df.copy()
        
    def set_dataframe_signos(self, df):
        """Setter del DataFrame Signos."""
        
        self.v.df_signos = df.copy()
    
    def sqlite_df(self):
        """DataFrame con los datos de la base de datos SQLite."""
        
        # Status bar.
        text = 'Abriendo proyecto.'
        self.v.status_bar(text)
        
        sqlite3 = self.get_sqlite3()
        
        ruta_db = self.ruta_db()
        
        try:
            sql_df = SQLitePandasDF(ruta_db, 'Proyecto')
            df_proyecto = sql_df.sql_to_df()
            self.set_dictionary_proyecto(df_proyecto)
            
            #sql_df = SQLitePandasDF(ruta_db, 'Implantaciones')
            #df = sql_df.sql_to_df()
            #self.set_dataframe_implantaciones(df)
            
            sql_df = SQLitePandasDF(ruta_db, 'Grupos')
            df = sql_df.sql_to_df()
            self.set_dataframe_grupos(df)
            
            sql_df = SQLitePandasDF(ruta_db, 'Relaciones')
            df = sql_df.sql_to_df()
            self.set_dataframe_relaciones(df)
            
            sql_df = SQLitePandasDF(ruta_db, 'Apoyos')
            df = sql_df.sql_to_df()
            self.set_dataframe_apoyos(df)
            
            sql_df = SQLitePandasDF(ruta_db, 'Ruedas')
            df = sql_df.sql_to_df()
            self.set_dataframe_ruedas(df)
            
            sql_df = SQLitePandasDF(ruta_db, 'Signos')
            df = sql_df.sql_to_df()
            self.set_dataframe_signos(df)
            
            print('\nsqlite_df.df_implantaciones')
            print(self.v.df_implantaciones)


        except sqlite3.Error as e:
            print('Error: {}'.format(e))
            self.v.message_box_db()
        
        # self.salida_datos()
        
        # return self.v.df
        
        # Status bar.
        text = 'Proyecto abierto.'
        self.v.status_bar(text)

    def ruta_db(self):
        """Ruta y nombre de la base de datos."""

        constantes = Constantes()
        subtitulo = constantes.get_abrir_datos()
        tipo_fichero = constantes.get_tipo_ficheros()
        pfad = FileDialog(subtitulo, '', tipo_fichero)
        ruta_nombre_db = pfad.get_open_file_name()
        
        return ruta_nombre_db

