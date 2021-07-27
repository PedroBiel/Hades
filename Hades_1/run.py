# -*- coding: utf-8 -*-
"""
HADES
Cargas para cuadro de cargas de implantación de máquinas
Created on %(date)s

__author__ = Pedro Biel
__version__ = 1.0.1
__email__ = pbiel@taimweser.com

Versión 1.0.1: Se incluye un mensaje de advertencia si no se puede guradar la
hoja Excel con las implantaciones.
"""


import pandas as pd
import qdarkstyle
import random
import sqlite3
import sys
import time
import xlsxwriter

from datetime import date

from PyQt5 import uic
from PyQt5.QtCore import QLibraryInfo, QLocale, QTranslator
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow

from dlg_proyecto.proyecto import DlgProyecto
from dlg_version.version import DlgVersion
from dlg_web.web import DlgWeb

from dlg_grupos.dlg_grupos import DlgGrupos
from dlg_relaciones.dlg_relaciones import DlgRelaciones
from dlg_apoyos.dlg_apoyos import DlgApoyos
from dlg_ruedas.dlg_ruedas import DlgRuedas
from dlg_signos.dlg_signos import DlgSignos

from dlg_fichero.cnt_dlgfichero import CntDlgFichero
from dlg_grupos.controlador.cnt_grupos import CntGrupos
from dlg_relaciones.controlador.cnt_relaciones import CntRelaciones
from dlg_apoyos.controlador.cnt_apoyos import CntApoyos
from dlg_ruedas.controlador.cnt_ruedas import CntRuedas
from dlg_signos.controlador.cnt_signos import CntSignos
from dlg_implantaciones.controlador.cnt_implantaciones import CntImplantaciones
from dlg_implantaciones.controlador.cnt_excel import CntExcel
from dlg_guardar.controlador.cnt_guarda_df_sql import CntGuardaDFSQL
from dlg_abrir.controlador.cnt_abre_sql_df import CntAbreSQLDF
from dlg_proyecto.controladores.cnt_proyecto import CntProyecto

from citas.cnt_citas import CntCitas

from pyqt5_recipes.messagebox import MessageBox

class MainWindow(QMainWindow):

    def __init__(self, parent=None):

        QMainWindow.__init__(self, parent)
        uic.loadUi('vistas/hades.ui', self)
        
        # Entorno virtual.
        print('\nEntorno virtual:', sys.prefix)
        print('python', sys.version)
        print('pandas', pd.__version__)
        print('qdarkstyle', qdarkstyle.__version__)
        print('xlsxwriter', xlsxwriter.__version__)
        
        # Icono y título de la ventana.
        self.setWindowIcon(QIcon("iconos/death_white.png"))
        self.setWindowTitle("Hades 1.0.0")
        
        # Librerías.
        self.pd = pd
        self.pd.set_option('display.width', 5000)  # Ancho del DataFrame.
        self.pd.set_option('display.max_columns', 20)  # Nº de columnas del DataFrame.
        self.random = random
        self.sqlite3 = sqlite3
        self.time = time
        self.xlsxwriter = xlsxwriter
        self.date = date
        
        # Parámetros.
        self.d_proyecto = {}  # Diccionario conlos datos del proyecto.
        self.ruta_nombre_db = ''  # Ruta y nombre de la base de datos SQLite.
        self.df_db = pd.DataFrame()  # Pandas DataFrame con los datos de la base de datos.
        self.df_db_shape = ''  # Dimensiones del DataFrame con los datos de la base de datos.
        self.df_db_tiempo = ''  # Tiempo en importar la base de datos y convertirla a pandas DataFrame.
        self.df_grupos = pd.DataFrame()  # Pandas DataFrame con los grupos.
        self.df_grupos_prev = pd.DataFrame()  # Pandas DataFrame con los grupos previos a la modificación.
        self.df_relaciones = pd.DataFrame()  # Pandas DataFrame con las relaciones.
        self.df_apoyos = pd.DataFrame()  # Pandas DataFrame con los apoyos.
        self.df_apoyos_prev = pd.DataFrame() # Pandas DataFrame con los apoyos previos a la modificación.
        self.df_ruedas = pd.DataFrame()  # Pandas DataFrame con el nº de ruedas.
        self.df_ruedas_prev = pd.DataFrame() # Pandas DataFrame con las ruedas previas a la modificación.
        self.df_signos = pd.DataFrame()  # Pandas DataFrame con los signos de las cargas.
        self.df_signos_prev = pd.DataFrame()  # Pandas DataFrame con los signos de las cargas previos a la midificación.
        self.df_implantaciones = pd.DataFrame()  # Pandas DataFrame con los datos para las implantaciones.
        self.df_impl_ap_gr = pd.DataFrame()  # Pandas DataFrame con los datos para las implantaciones.
        self.df_impl_ap_gr_modelo = pd.DataFrame()  # Pandas DataFrame con los datos para las implantaciones.
        self.df_impl_gr_ap = pd.DataFrame()  # Pandas DataFrame con los datos para las implantaciones.
        self.df_impl_gr_ap_modelo = pd.DataFrame()  # Pandas DataFrame con los datos para las implantaciones.
        self.ruta_nombre_xlsx = ''  # Ruta y nombre de la hoja Excel.
        self.xlsx_tiempo = 0  # Tiempo en exportar las implantaciones y convertirla a Excel.
        self.cita = ''  # Cita memorable
        
        # Widgets PyQt5.
        
        # MENÚ
        # ====
        
        # Proyecto.
        self.axn_abrir = self.actionAbrir
        self.axn_guardar = self.actionGuardar
        self.axn_proyecto = self.actionProyecto
        self.axn_about = self.actionAcerca_de_Hades
        self.axn_version = self.actionRevisiones
        
        # Instancias de clases.
        self.cnt_abrir = CntAbreSQLDF(self)
        self.cnt_guardar = CntGuardaDFSQL(self)
        self.cnt_proyecto = CntProyecto(self)
        self.dlg_proyecto = DlgProyecto(self)
        self.dlg_web = DlgWeb(self)
        self.dlg_version = DlgVersion(self)
        
        # Eventos.
        self.axn_abrir.triggered.connect(self.cnt_abrir.sqlite_df)
        self.axn_abrir.triggered.connect(self.proyecto_abierto)
        self.axn_guardar.triggered.connect(self.cnt_guardar.df_sqlite)
        self.axn_proyecto.triggered.connect(self.call_proyecto)
        self.axn_about.triggered.connect(self.call_dialog_web)
        self.axn_version.triggered.connect(self.call_dialog_version)
        
        # HADES
        # =====
        
        self.btn_db = self.pushButtonRutaNombreDB
        self.btn_db.setShortcut('Ctrl+B')
        self.btn_db.setToolTip('Importa la base de datos con las reacciones\
| Ctrl+B')
        self.lbl_db = self.labelRutaNombreDB
        self.lbl_tiempo = self.labelTiempo
        self.lbl_dimensiones = self.labelDimensiones
        fuente = QFont()
        fuente.setFamily('Consolas')
        fuente.setPointSize(8)
        self.lbl_db.setFont(fuente)
        self.lbl_tiempo.setFont(fuente)
        self.lbl_dimensiones.setFont(fuente)
        
        self.btn_grupos = self.pushButtonGrupos
        self.btn_grupos.setShortcut('Ctrl+G')
        self.btn_grupos.setToolTip('Asigna los grupos con los casos | Ctrl+G')
        
        self.btn_relaciones = self.pushButtonRelaciones
        self.btn_relaciones.setShortcut('Ctrl+R')
        self.btn_relaciones.setToolTip(
            'Asigna las relaciones, los coeficientes de mayoración y el \
redondeo de los grupos | Ctrl+R'
            )
        
        self.btn_apoyos = self.pushButtonApoyos
        self.btn_apoyos.setShortcut('Ctrl+A')
        self.btn_apoyos.setToolTip(
            'Asigna el nombre de los apoyos a los nudos | Ctrl+A'
            )
        
        self.btn_ruedas = self.pushButtonNRuedas
        self.btn_ruedas.setShortcut('Ctrl+N')
        self.btn_ruedas.setToolTip(
            'Asigna la cantidad de ruedas a los apoyos | Ctrl+N'
            )
        
        self.btn_signos = self.pushButtonSignos
        self.btn_signos.setShortcut('Ctrl+S')
        self.btn_signos.setToolTip(
            'Asigna los signos a las cargas | Ctrl+S'
            )
        
        self.btn_implantaciones = self.pushButtonImplantaciones
        self.btn_implantaciones.setShortcut('Ctrl+I')
        self.btn_implantaciones.setToolTip(
            'Crea hoja Excel con los cuadros de implantaciones | Ctrl+I'
            )
        self.lbl_xlsx = self.labelRutaNombreExcel
        self.lbl_tiempo_xlsx = self.labelTiempoExcel
        self.lbl_xlsx.setFont(fuente)
        self.lbl_tiempo_xlsx.setFont(fuente)
        
        self.btn_cerrar = self.pushButtonCerrar
        self.btn_cerrar.setShortcut('Ctrl+Q')
        self.btn_cerrar.setToolTip('Cierra la aplicación | Ctrl+Q')
        
        self.txt_cita = self.textEditCita
        self.txt_cita.setFont(fuente)
        
        # Instancias de clase.
        self.cnt_dlg_fichero = CntDlgFichero(self)
        self.cnt_grupos = CntGrupos(self)
        self.cnt_relaciones = CntRelaciones(self)
        self.cnt_apoyos = CntApoyos(self)
        self.cnt_ruedas = CntRuedas(self)
        self.cnt_signos = CntSignos(self)
        self.cnt_implantaciones = CntImplantaciones(self)
        self.cnt_excel = CntExcel(self)
        self.cnt_citas = CntCitas(self)
        
        # Eventos para buscar el directorio y el nombre de la base de datos.
        self.btn_db.clicked.connect(self.cnt_dlg_fichero.get_ruta_nombre_db)
        
        # Eventos para crear los grupos.
        self.btn_grupos.clicked.connect(self.cnt_grupos.crea_grupos)
        
        # Eventos para asignar las relaciones a los grupos.
        self.btn_relaciones.clicked.connect(
            self.cnt_relaciones.crea_relaciones
            )
        
        # Eventos para asignar el nombre del apoyo a los nudos.
        self.btn_apoyos.clicked.connect(self.cnt_apoyos.crea_apoyos)
        
        # Eventos para asignar el número de ruedas a los apoyos.
        self.btn_ruedas.clicked.connect(self.cnt_ruedas.crea_ruedas)
        
        # Eventos para asignar los signos de las ruedas.
        self.btn_signos.clicked.connect(self.cnt_signos.crea_signos)
        
        # Eventos para crear el cuadro de implantaciones.
        self.btn_implantaciones.clicked.connect(self.set_project)
        self.btn_implantaciones.clicked.connect(
            self.cnt_implantaciones.crea_implantaciones
            )
        self.btn_implantaciones.clicked.connect(
            self.cnt_excel.get_save_file_name
            )
        self.btn_implantaciones.clicked.connect(
            self.cnt_excel.crea_excel_implantaciones
            )

        # Cerrar la aplicación.
        self.btn_cerrar.clicked.connect(self.cierra_aplicacion)
        
        # Cita.
        self.cnt_citas.cita()
        self.salida_cita()
        
    # Salidas PyQt5.
    
    def status_bar(self, text):
        """Texto informativo en status bar."""
        
        self.statusbar.setFont(QFont('Consolas', 8))
        self.statusbar.showMessage(text)
        
    def salida_ruta_nombre_db(self):
        """Salida de la ruta y el nombre de la base de datos."""
        
        self.lbl_db.setText(self.ruta_nombre_db)
        self.lbl_dimensiones.setText(self.df_db_shape)
        self.lbl_tiempo.setText(self.df_db_tiempo)
        
    def call_dialogo_grupos(self, df, model):
        """Llama al diálogo de Grupos."""
        
        self.dlg_grupos = DlgGrupos(parent=self, df=df, model=model)
        self.dlg_grupos.show()
        
    def call_dialogo_relaciones(self, df, model):
        """Llama al diálogo de Relaciones."""
        
        self.dlg_relaciones = DlgRelaciones(parent=self, df=df, model=model)
        self.dlg_relaciones.show()
    
    def call_dialogo_apoyos(self, df, model):
        """Llama al diálogo de Apoyos."""
        
        self.dlg_apoyos = DlgApoyos(parent=self, df=df, model=model)
        self.dlg_apoyos.show()

    def call_dialogo_ruedas(self, df, model):
        """Llama al diálogo de Ruedas."""
        
        self.dlg_ruedas = DlgRuedas(parent=self, df=df, model=model)
        self.dlg_ruedas.show()

    def call_dialogo_signos(self, df, model):
        """Llama al diálogo de Signos."""
        
        self.dlg_signos = DlgSignos(parent=self, df=df, model=model)
        self.dlg_signos.show()
        
    def salida_ruta_nombre_xlsx(self):
        """Salida de la ruta y el nombre de la hoja Excel."""
        
        self.lbl_xlsx.setText(self.ruta_nombre_xlsx)
        self.lbl_tiempo_xlsx.setText(self.xlsx_tiempo)
        
    def salida_cita(self):
        """Salida de la cita."""
        
        self.txt_cita.setText(self.cita)
        
    # Eventos del Menú.
    
    # Evento para llamar al diálogo del proyecto.
    def call_proyecto(self):
        """Call the Dialog Proyecto."""
        
        # self.dlg_proyecto.show()
        self.dlg_proyecto = DlgProyecto(parent=self, d=self.d_proyecto)
        # self.d_proyecto = self.dlg_proyecto.get_diccionario_proyecto()
        self.d_proyecto = self.dlg_proyecto.proyecto()
        # print('d_proyecto 1', self.d_proyecto)
        self.dlg_proyecto.show()
        
    def get_project(self):
        """Getter de los datos de proyecto."""

        dlg = self.dlg_proyecto
        proyecto = dlg.proyecto()
        
        return proyecto
    
    def set_project(self):
        """Setter de los datos de proyecto."""
        
        self.d_proyecto = self.get_project()
        
    def proyecto_abierto(self):
        # print('d_proyecto 2', self.d_proyecto)
        self.dlg_proyecto = DlgProyecto(parent=self, d=self.d_proyecto)
        # self.d_proyecto = dlg_proyecto.get_diccionario_proyecto()
        self.d_proyecto = self.dlg_proyecto.proyecto()
        # print('d_proyecto 3', self.d_proyecto)
        # dlg_proyecto.show()
        # self.cnt_proyecto.datos_proyecto_abierto(self.d_proyecto)
    
    # Evento para llamar al diálogo web.
    def call_dialog_web(self):
        """Call the Dialog Web."""

        self.dlg_web.show()
    
    # Evento para llamar al diálogo Versión.
    def call_dialog_version(self):
        """Call the Dialog Version."""

        self.dlg_version.show()
    
    # Evento para guardar datos.
    def message_box(self):
        """https://www.tutorialspoint.com/pyqt/pyqt_qmessagebox.htm"""
        
        window_title = 'Advertencia'
        text = 'Faltan datos por introducir.'
        info_text = 'Comprueba de nuevo las entradas de datos.'
        self.messagebox = MessageBox(window_title, text, info_text)
        self.messagebox.warning()
       
    # Evento para abrir datos.
    def message_box_db(self):
        """https://www.tutorialspoint.com/pyqt/pyqt_qmessagebox.htm"""
        
        window_title = 'Advertencia'
        text = 'Hay un problema con la base de datos.'
        info_text = 'Comprueba de nuevo las entradas de datos.'
        self.messagebox = MessageBox(window_title, text, info_text)
        self.messagebox.warning()
        
    # Evento para guardar datos en Excel.
    def message_box_db(self):
        """https://www.tutorialspoint.com/pyqt/pyqt_qmessagebox.htm"""
        
        window_title = 'Advertencia'
        text = 'Hay un problema al guardar la hoja Excel.'
        info_text = 'Comprueba que la hoja Excel no esté abierta.'
        self.messagebox = MessageBox(window_title, text, info_text)
        self.messagebox.warning()

    def cierra_aplicacion(self):
        """Cierra todas las ventanas de la aplicación."""
        
        try:
            self.dlg_grupos.close()
            self.dlg_relaciones.close()
            self.dlg_apoyos.close()
            self.dlg_ruedas.close()
            self.dlg_signos.close()
            self.dlg_proyecto.close()
            # self.dlg_coefs.close()
            self.close()
        except:
            self.close()
            
        # %clear  # Limpia terminal de IPython.


if __name__ == '__main__':

    app = QApplication(sys.argv)

    # Traducir el idiona del sistema operativo y texto predeterminado de PyQt.
    qt_translator = QTranslator()
    qt_translator.load(
        'qtbase_' + QLocale.system().name(),
        QLibraryInfo.location(QLibraryInfo.TranslationsPath)
        )
    app.installTranslator(qt_translator)

    # Dark style.
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())

    # Fuente.
    fuente = QFont()
    fuente.setFamily('Consolas')
    fuente.setPointSize(11)
    app.setFont(fuente)
    
    # Ejecuta aplicación.
    myapp = MainWindow()
    myapp.show()
    sys.exit(app.exec_())
