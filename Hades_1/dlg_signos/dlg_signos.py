# -*- coding: utf-8 -*-
"""
HADES
Diálogo Grupos

Created on Wed Sep  9 14:27:24 2020

__author__ = Pedro Biel
__version__ = 0.0.0
__email__ = pbiel@taimweser.com
"""


import pandas as pd

from PyQt5 import uic
from PyQt5.QtWidgets import QAbstractScrollArea, QDialog

from pyqt5_recipes.messagebox import MessageBox


class DlgSignos(QDialog):
    
    def __init__(self, parent=None, df=None, model=None):
        """
        Diálogo Grupos de la aplicación.
        
        Para pasar datos de QMainWindow a QDialog:
        https://stackoverflow.com/questions/14309703/passing-parameter-from-main-window-to-pop-up-qdialog-window
        """
        
        QDialog.__init__(self, parent)
        uic.loadUi('dlg_signos/vista/dlg_signos.ui', self)
        
        self.df = df  # self.v.df_signos
        self.model = model
        
        # Widgets PyQt5.
        self.lbl_1 = self.label_1
        self.lbl_2 = self.label_2
        self.lbl_3 = self.label_3
        self.lbl_4 = self.label_4
        self.lbl_5 = self.label_5
        self.lbl_6 = self.label_6
        self.tbl = self.tableView
        self.btn_aceptar = self.pushButtonAceptar
        
        # Título de la ventana.
        self.setWindowTitle('Grupos')
        
        # Altura mínima de la ventana.
        self.setMinimumHeight(500)
        
        # Texto de etiquetas.
        self.lbl_1.setText('Si las direcciones de los ejes RSA y de implantación coinciden:')
        self.lbl_2.setText('  signo = -1')
        self.lbl_3.setText('Si las direcciones de los ejes RSA y de implantación no coinciden:')
        self.lbl_4.setText('  signo = 1')
        self.lbl_5.setText('Si la carga no aplica (p. e. no hay momentos):')
        self.lbl_6.setText('  signo = 0')

        # Modelo de la tabla.
        self.tbl.setModel(self.model)
        # Ajusta el ancho de las columnas a los contenidos.
        self.tbl.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tbl.resizeColumnsToContents()
        
        # Botones.
        self.btn_aceptar.setText('Aceptar cambios')
        self.btn_aceptar.setShortcut('Ctrl+S')
        self.btn_aceptar.setToolTip('Acepta los cambios en la tabla | Ctrl+S')
        
        # Eventos.
        self.btn_aceptar.clicked.connect(self.acepta_cambios)
        
    def acepta_cambios(self):
        """
        Comprueba si las entradas en columna Signos son válidas, si no, 
        lanza un MessageBox.
        Acepta los cambios realizados en la QTableView y cierra el diálogo.
        """
        
        # # Convierte el tipo de datos del DataFrame a ints.
        # self.df = self.df_astype(self.df)
        
        # Comprueba si las entradas en columnas Signos son válidas.
        signos_validos = self.entradas_signo_validos(self.df)
        
        if not signos_validos:
            window_title = 'Advertencia'
            text = 'Signo no válido.'
            info_text = 'Comprueba de nuevo las entradas de datos.'
            self.message_box(window_title, text, info_text)
        else:
            # Cierra el diálogo.
            self.reject()
        
        print('\ndf_signos:')
        print(self.df)
    
    def entradas_signo_validos(self, df):
        """
        Comprueba que las entradas en las columnas son válidas.
        Devuelve True o False.
        """
        try:
            df = self.df_astype(df)
        except Exception as e:
            print('Exception en DlgSignos.entradas_signo_validos()', e)
        
        cols = [
            'signo_Fx', 'signo_Fy', 'signo_Fz',
            'signo_Mx', 'signo_My', 'signo_Mz'
            ]
        signos_validos = [-1, 0, 1]
        check = df[cols].isin(signos_validos).all()
        valido = check.all() == True
        
        return valido
    
    def df_astype(self, df):
        """
        Convierte el tipo de datos de las columnas del Dataframe.

        Returns
        -------
        df : objeto pandas DataFrame
        """
        
        cols = [
            'signo_Fx', 'signo_Fy', 'signo_Fz',
            'signo_Mx', 'signo_My', 'signo_Mz'
            ]
        for col in cols:
            df[col] = df[col].astype(int)

        return df.copy()    
    
    def message_box(self, window_title, text, info_text):
        """https://www.tutorialspoint.com/pyqt/pyqt_qmessagebox.htm"""
        
        self.messagebox = MessageBox(window_title, text, info_text)
        self.messagebox.warning()
