 # -*- coding: utf-8 -*-
"""
HADES
Controlador de guardar datos de pandas DataFrame a SQLite

Created on Tue Feb 23 13:33 2021

__author__ = Pedro Biel
__version__ = 1.0.0
__email__ = structural.eng.biel@gmail.com
"""


from pyqt5_clases.qfiledialog import FileDialog

from transferenciadatos.pandasdfsqlite import PandasDFSQLite

from dlg_fichero.constantes_dlgfichero import Constantes


class CntGuardaDFSQL:
    """Controlador de guardar datos de pandas DataFrame a SQLite."""
    
    def __init__(self, ventana):
        self.v = ventana
        
    def get_pandas(self):
        """Getter de la librería pandas."""
        
        return self.v.pd
    
    def get_sqlite3(self):
        """Getter de la librería sqlite3."""
        
        return self.v.sqlite3
    
    def get_proyecto(self):
        """Getter de los datos del proyecto."""
        
        return self.v.d_proyecto.copy()
    
    def get_dataframe_implantaciones(self):
        """Getter del DataFrame Implantaciones."""
        
        return self.v.df_implantaciones.copy()
    
    def get_dataframe_grupos(self):
        """Getter del DataFrame Grupos."""
        
        return self.v.df_grupos.copy()
    
    def get_dataframe_apoyos(self):
        """Getter del DataFrame Apoyos."""
        
        return self.v.df_apoyos.copy()
    
    def get_dataframe_relaciones(self):
        """Getter del DataFrame Raleciones."""
        
        return self.v.df_relaciones.copy()
    
    def get_dataframe_ruedas(self):
        """Getter del DataFrame Ruedas."""
        
        return self.v.df_ruedas.copy()
        
    def get_dataframe_signos(self):
        """Getter del DataFrame Signos de las cargas."""
        
        return self.v.df_signos.copy()
    
    def dataframe_proyecto(self):
        """
        Pasa los datos del diccionario con los datos de proyecto a un
        DataFrame de pandas.
        """
        
        pd = self.get_pandas()
        d_proyecto = self.get_proyecto()
        ser = pd.Series(d_proyecto)
        df = ser.to_frame()
        df = df.T
        
        return df
        
    def get_save_file_name(self):
        """
        Obtiene la ruta y el nombre del fichero a guardar de FileDialog.
        Type : str
        """
        
        constantes = Constantes()
        subtitulo = constantes.get_guardar_datos()
        tipo_fichero = constantes.get_tipo_ficheros()
        pfad = FileDialog(subtitulo, '', tipo_fichero)
        # self.set_ruta_nombre_db(pfad.get_save_file_name())
        ruta_nombre_db = pfad.get_save_file_name()
        
        return ruta_nombre_db
    
    def df_sqlite(self):
        """Base de datos SQLite con los datos del DataFrame.""" 
        
        # Status bar.
        text = 'Guardando proyecto.'
        self.v.status_bar(text)
        
        sqlite3 = self.get_sqlite3()
        
        df_proyecto = self.dataframe_proyecto()
        df_implantaciones = self.get_dataframe_implantaciones()
        df_grupos = self.get_dataframe_grupos()
        df_relaciones = self.get_dataframe_relaciones()
        df_apoyos = self.get_dataframe_apoyos()
        df_ruedas = self.get_dataframe_ruedas()
        df_signos = self.get_dataframe_signos()
        
        if df_proyecto.empty or df_implantaciones.empty or df_grupos.empty or\
            df_relaciones.empty or df_apoyos.empty or df_ruedas.empty or\
            df_signos.empty:
                
            self.v.message_box()
            
        else:
            ruta = self.get_save_file_name()
            
            try:
                df_sql = PandasDFSQLite(ruta, df_proyecto, 'Proyecto')
                df_sql.df_to_sql()
                df_sql = PandasDFSQLite(
                    ruta, df_implantaciones, 'Implantaciones'
                    )
                df_sql.df_to_sql()
                df_sql = PandasDFSQLite(ruta, df_grupos, 'Grupos')
                df_sql.df_to_sql()
                df_sql = PandasDFSQLite(ruta, df_relaciones, 'Relaciones')
                df_sql.df_to_sql()
                df_sql = PandasDFSQLite(ruta, df_apoyos, 'Apoyos')
                df_sql.df_to_sql()
                df_sql = PandasDFSQLite(ruta, df_ruedas, 'Ruedas')
                df_sql.df_to_sql()
                df_sql = PandasDFSQLite(ruta, df_signos, 'Signos')
                df_sql.df_to_sql()
            
            except sqlite3.Error as e:
                print('Error: {}'.format(e))
                self.v.message_box()
                
        # Status bar.
        text = 'Proyecto guardado.'
        self.v.status_bar(text)
        