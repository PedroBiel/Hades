# -*- coding: utf-8 -*-
"""
HADES
Diálogo Coeficientes

Created on Wed Oct  28 14:35 2020

__author__ = Pedro Biel
__version__ = 0.0.0
__email__ = pbiel@taimweser.com
"""


import pandas as pd

from PyQt5 import uic
from PyQt5.QtWidgets import QAbstractScrollArea, QDialog

from pyqt5_recipes.messagebox import MessageBox


class DlgCoeficientes(QDialog):
    
    def __init__(self, parent=None, df=None, model=None):
        """
        Diálogo Coeficientes de la aplicación.
        
        Para pasar datos de QMainWindow a QDialog:
        https://stackoverflow.com/questions/14309703/passing-parameter-from-main-window-to-pop-up-qdialog-window
        """
        
        QDialog.__init__(self, parent)
        uic.loadUi('dlg_coeficientes/vista/dlg_coeficientes.ui', self)
        
        self.df = df  # self.v.df_coeficientes
        self.model = model
        
        # Widgets PyQt5.
        self.lbl_1 = self.label_1
        self.lbl_2 = self.label_2
        self.tbl = self.tableView
        self.btn_aceptar = self.pushButtonAceptar
        
        # Título de la ventana.
        self.setWindowTitle('Coeficientes de mayoración y redondeos')
        
        # Altura mínima de la ventana.
        self.setMinimumHeight(500)
        
        # Texto de etiquetas.
        self.lbl_1.setText('Indicar el Coeficiente de mayoración por cada Grupo.')
        self.lbl_2.setText('Indicar el Redondeo por cada Grupo.')

        # Modelo de la tabla.
        self.tbl.setModel(self.model)
        # Ajusta el ancho de las columnas a los contenidos.
        self.tbl.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tbl.resizeColumnsToContents()
        
        # Botones.
        self.btn_aceptar.setText('Aceptar cambios')
        self.btn_aceptar.setShortcut('Ctrl+A')
        self.btn_aceptar.setToolTip('Acepta los cambios en la tabla | Ctrl+A')
        
        # Eventos.
        self.btn_aceptar.clicked.connect(self.acepta_cambios)
        
    def acepta_cambios(self):
        """
        Comprueba si las entradas en columnas Coeficiente y Redondeo son 
        válidas, si no, lanza un MessageBox.
        Acepta los cambios realizados en la QTableView y cierra el diálogo.
        """
        
        # Comprueba si las entradas en columnas Coeficiente y Redondeo son válidas.
        col = 'Mayoración'
        coeficientes_validos = self.entradas_validas(self.df, col)
        col = 'Redondeo'
        redondeos_validos = self.entradas_validas(self.df, col)

        if not coeficientes_validos:
            window_title = 'Advertencia'
            text = 'Coeficiente no válido.'
            info_text = 'Comprueba de nuevo las entradas de datos.'
            self.message_box(window_title, text, info_text)
        elif not redondeos_validos:
            window_title = 'Advertencia'
            text = 'Redondeo no válido.'
            info_text = 'Comprueba de nuevo las entradas de datos.'
            self.message_box(window_title, text, info_text)
        else:
            # Cierra el diálogo.
            self.reject()
            
        print('\ndf_coeficientes:')
        print(self.df)
    
    def entradas_validas(self, df, col):
        """
        Comprueba que las entradas en la columna 'col' son válidas.
        Devuelve True o False.
        """
        
        valido = pd.to_numeric(df[col], errors='coerce').notnull().all()
        
        return valido
    
    def message_box(self, window_title, text, info_text):
        """https://www.tutorialspoint.com/pyqt/pyqt_qmessagebox.htm"""
        
        self.messagebox = MessageBox(window_title, text, info_text)
        self.messagebox.warning()
