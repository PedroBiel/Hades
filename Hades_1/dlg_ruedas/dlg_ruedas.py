# -*- coding: utf-8 -*-
"""
HADES
Diálogo Ruedas

Created on Wed Sep  9 14:27:24 2020

__author__ = Pedro Biel
__version__ = 0.0.0
__email__ = pbiel@taimweser.com
"""


import pandas as pd

from PyQt5 import uic
from PyQt5.QtWidgets import QAbstractScrollArea, QDialog

from pyqt5_recipes.messagebox import MessageBox


class DlgRuedas(QDialog):
    
    def __init__(self, parent=None, df=None, model=None):
        """
        Diálogo Nº Ruedas de la aplicación.
        
        Para pasar datos de QMainWindow a QDialog:
        https://stackoverflow.com/questions/14309703/passing-parameter-from-main-window-to-pop-up-qdialog-window
        """
        
        QDialog.__init__(self, parent)
        uic.loadUi('dlg_ruedas/vista/dlg_ruedas.ui', self)
        
        self.df = df  # self.v.df_ruedas
        self.model = model
        
        # Widgets PyQt5.
        self.lbl_1 = self.label_1
        self.lbl_2 = self.label_2
        self.tbl = self.tableView
        self.btn_aceptar = self.pushButtonAceptar
        
        # Título de la ventana.
        self.setWindowTitle('Nº de Ruedas')
        
        # Altura mínima de la ventana.
        self.setMinimumHeight(500)
        
        # Texto de etiquetas.
        self.lbl_1.setText('Indicar la cantidad de Ruedas por cada Apoyo.')
        self.lbl_2.setText('Nº de ruedas = entero ≥ 1.')
        
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
        Comprueba si las entradas en columna Ruedas son válidas, si no, 
        lanza un MessageBox.
        Acepta los cambios realizados en la QTableView y cierra el diálogo.
        """
        
        # Comprueba si las entradas en columna Ruedas son numéricas.
        col = 'Ruedas'
        ruedas_validas_1 = self.entradas_ruedas_numericas(self.df, col)
        
        if not ruedas_validas_1:
            window_title = 'Advertencia'
            text = 'Nº de ruedas no válido.'
            info_text = 'Comprueba de nuevo las entradas de datos.'
            self.message_box(window_title, text, info_text)
        # else:
        #     # Cierra el diálogo.
        #     self.reject()
        
        
        # Comprueba si las entradas en columna Ruedas son mayor que 0.
        try:
            ruedas_validas_2 = self.entradas_ruedas_mayor_0(self.df, col)
        except ValueError as e:
            print('ValueError en DlgRuedas.acepta_cambios():', e)
            ruedas_validas_2 = False
        
        if not ruedas_validas_2:
            window_title = 'Advertencia'
            text = 'Nº de ruedas no válido.'
            info_text = 'Comprueba de nuevo las entradas de datos.'
            self.message_box(window_title, text, info_text)
        else:
            # Cierra el diálogo.
            self.reject()
            
        print('\ndf_ruedas:')
        print(self.df)
    
    def entradas_ruedas_numericas(self, df, col):
        """
        Comprueba que las entradas en la columna 'col' son numéricas.
        Devuelve True o False.
        """
        
        valido = pd.to_numeric(df[col], errors='coerce').notnull().all()
        
        return valido
    
    def entradas_ruedas_mayor_0(self, df, col):
        """
        Comprueba que las entradas en la columna 'col' son mayores que 0.
        Devuelve True o False.
        """
        
        self.df[col] = self.df[col].replace(',', '.').astype(int)
        valido = df[col].gt(0).all()
        
        return valido
    
    
    def message_box(self, window_title, text, info_text):
        """https://www.tutorialspoint.com/pyqt/pyqt_qmessagebox.htm"""
        
        self.messagebox = MessageBox(window_title, text, info_text)
        self.messagebox.warning()
