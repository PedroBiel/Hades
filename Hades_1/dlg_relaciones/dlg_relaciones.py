# -*- coding: utf-8 -*-
"""
HADES
Diálogo Relaciones

Created on Fri Oct  2 12:15 2020

__author__ = Pedro Biel
__version__ = 0.0.0
__email__ = pbiel@taimweser.com
"""


import pandas as pd

from PyQt5 import uic
from PyQt5.QtWidgets import QAbstractScrollArea, QDialog

from pyqt5_recipes.messagebox import MessageBox


class DlgRelaciones(QDialog):
    
    def __init__(self, parent=None, df=None, model=None):
        """
        Diálogo Relaciones de la aplicación.
        
        Para pasar datos de QMainWindow a QDialog:
        https://stackoverflow.com/questions/14309703/passing-parameter-from-main-window-to-pop-up-qdialog-window
        """
        
        QDialog.__init__(self, parent)
        uic.loadUi('dlg_relaciones/vista/dlg_relaciones.ui', self)
        
        self.df = df  # self.v.df_relaciones
        self.model = model
        
        # Widgets PyQt5.
        self.lbl_1 = self.label_1
        self.lbl_2 = self.label_2
        self.lbl_3 = self.label_3
        self.lbl_4 = self.label_4
        self.lbl_5 = self.label_5
        self.lbl_6 = self.label_6
        self.lbl_7 = self.label_7
        self.lbl_8 = self.label_8
        self.lbl_9 = self.label_9
        self.tbl = self.tableView
        self.btn_aceptar = self.pushButtonAceptar
        
        # Título de la ventana.
        self.setWindowTitle(
            'Relaciones, coeficientes de mayoración y redondeos'
            )
        
        # Altura mínima de la ventana.
        self.setMinimumHeight(500)
        
        # Texto de etiquetas.
        self.lbl_1.setText(
            'Relación Y  -> valores máx. y mín. de la suma de todos los casos del grupo'
            )
        self.lbl_2.setText(
            '               (p.e. Cargas Permanentes).'
            )
        self.lbl_3.setText(
            'Relación O  -> valores máx. y mín. de los casos individuales del grupo'
            )
        self.lbl_4.setText(
            '               (p.e. Viento).'
            )
        self.lbl_5.setText(
            'Relación YO -> valores máx. y mín. de entre la suma de todos los casos'
            )
        self.lbl_6.setText(
            '               y de los casos individuales del grupo (p.e. Sobrecargas).'
            )
        self.lbl_7.setText(
            'Relaciones diferentes de Y, O, YO no se tendrán en cuenta.'
            )
        self.lbl_8.setText(
            'Indicar el Coeficiente de mayoración para cada Grupo.'
            )
        self.lbl_9.setText('Indicar el Redondeo para cada Grupo.')
        
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
        Comprueba si las entradas en columnas Relación, Mayoración y Redondeo 
        son válidas, si no, lanza un MessageBox.
        Acepta los cambios realizados en la QTableView y cierra el diálogo.
        """   
    
        # Comprueba si las entradas en columnas Realción, Mayoración y Redondeo son válidas.
        col = 'Relación'
        relaciones_validas = self.entradas_relacion_validas(self.df, col)
        col = 'Mayoración'
        coeficientes_validos = self.entradas_validas(self.df, col)
        col = 'Redondeo'
        redondeos_validos = self.entradas_validas(self.df, col)
        
        if not relaciones_validas:
            window_title = 'Advertencia'
            text = 'Relación no válida.'
            info_text = 'Comprueba de nuevo las entradas de datos.'
            self.message_box(window_title, text, info_text)
        elif not coeficientes_validos:
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
            
        print('\ndf_relaciones:')
        print(self.df)
        
    def entradas_relacion_validas(self, df, col):
        """
        Comprueba que las entradas en la columna 'col' son válidas.
        Devuelve True o False.
        """
        
        relaciones_validas = ['Y', 'y', 'O', 'o', 'YO', 'yo']
        check = df[col].isin(relaciones_validas)
        valido = check.all() == True
        
        return valido
    
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
