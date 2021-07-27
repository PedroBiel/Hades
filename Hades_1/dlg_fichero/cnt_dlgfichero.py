# -*- coding: utf-8 -*-
"""
HADES
Controlador del diálogo de fichero

Created on Mon Jul 27 13:48:29 2020

__author__ = Pedro Biel
__version__ = 0.0.0
__email__ = pbiel@taimweser.com
"""


from pyqt5_clases.qfiledialog import FileDialog

from dlg_fichero.constantes_dlgfichero import Constantes
from dlg_fichero.datos_dlgfichero import ConvierteTiposDF
from transferenciadatos.sqlitepandasdf import SQLitePandasDF

#import time

class CntDlgFichero:
    """
    Controlador de la clase QFileDialog proporciona un cuadro de diálogo que 
    permite seleccionar archivos o directorios.
    """
    
    def __init__(self, ventana):
        """
        Crea la ventana de MainWindow.
        Crea el tiempo de inicio t0 y el tiempo de finalización t1 del proceso.
        """
        
        self.v = ventana
        
        self.t0 = ''
        self.t1 = ''
        
    def get_ruta_nombre_db(self):
        """
        Obtiene la ruta y el nombre del fichero a abrir de FileDialog.
        Type : str
        """
        
        # Status bar.
        text = 'Seleccionando base de datos SQLite para las implantaciones...'
        self.v.status_bar(text)
        
        # Resetea labels.
        self.v.ruta_nombre_db = '_'
        self.v.df_db_shape = '_'
        self.v.df_db_tiempo = '_'
        self.v.salida_ruta_nombre_db()
        
        # Reinicia DataFrames.
        self.v.df_grupos = self.v.pd.DataFrame()
        self.v.df_relaciones = self.v.pd.DataFrame()
        self.v.df_apoyos = self.v.pd.DataFrame()
        self.v.df_ruedas = self.v.pd.DataFrame()
        self.v.df_signos = self.v.pd.DataFrame()
        # self.v.df_coeficientes = self.v.pd.DataFrame()
        
        # Ruta y nombre de la base de datos.
        constantes = Constantes()
        subtitulo = constantes.get_abrir_datos()
        tipo_fichero = constantes.get_tipo_ficheros()
        pfad = FileDialog(subtitulo, '', tipo_fichero)
        
        self.v.ruta_nombre_db = pfad.get_open_file_name()
        
        # Transfiere datos a DataFrame.
        self.transfiere_datos_df()
        
        # Salida PyQt5.
        self.v.salida_ruta_nombre_db()
        
        # Status bar.
        text = 'Base de datos SQLite para las implantaciones importada con éxito.'
        self.v.status_bar(text)
        
    def transfiere_datos_df(self):
        """
        Transfiere los datos de la base de datos SQLite a un DataFrame de 
        pandas.

        Returns
        -------
        df_db : objeto pandas DataFrame
        """
        
        # Inicia cronómetro.
        #self.t0 = self.v.time.clock()
        self.t0 = self.v.time.perf_counter()
        
        # Transfiere datos a DataFrame.
        self.v.df_db = self.sql_pandas_df()
        
        # Convierte el tipo de valores del DataFrame.
        convierte = ConvierteTiposDF(self.v.df_db)
        self.v.df_db = convierte.tipo_valores()
        print('\ndf_db')
        print(self.v.df_db)
        print(self.v.df_db.dtypes)
        
        # Nº de filas y columnas del DataFrame.
        filas = str(self.v.df_db.shape[0])
        columnas = str(self.v.df_db.shape[1])
        self.v.df_db_shape = filas + ' filas * ' + columnas + ' columnas'
        
        # Cronometra.
        #self.t1 = self.v.time.clock()
        self.t1 = self.v.time.perf_counter()
        t = round((self.t1 - self.t0), 2)
        self.v.df_db_tiempo = str(t) + ' s'

    def sql_pandas_df(self):
        """
        Contecta con la base de datos SQLite y transfiere los datos a un 
        pandas DataFrame.

        Returns
        -------
        df : object
            Pandas DataFrame con los datos de la base de datos.
        """
        
        sql_df = SQLitePandasDF(self.v.ruta_nombre_db, 'Reacciones')
        df = sql_df.sql_to_df()
        
        return df
        