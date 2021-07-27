# -*- coding: utf-8 -*-
"""
HADES
Diálogo Apoyos

Created on Fri Oct  2 12:15 2020

__author__ = Pedro Biel
__version__ = 0.0.0
__email__ = pbiel@taimweser.com
"""


from PyQt5 import uic
from PyQt5.QtWidgets import QAbstractScrollArea, QDialog


class DlgApoyos(QDialog):
    
    def __init__(self, parent=None, df=None, model=None):
        """
        Diálogo Relaciones de la aplicación.
        
        Para pasar datos de QMainWindow a QDialog:
        https://stackoverflow.com/questions/14309703/passing-parameter-from-main-window-to-pop-up-qdialog-window
        """
        
        QDialog.__init__(self, parent)
        uic.loadUi('dlg_apoyos/vista/dlg_apoyoss.ui', self)
        
        self.df = df  # self.v.df_apoyos
        self.model = model
        
        # Widgets PyQt5.
        self.lbl_1 = self.label_1
        self.tbl = self.tableView
        self.btn_aceptar = self.pushButtonAceptar
        
        # Título de la ventana.
        self.setWindowTitle('Apoyos')
        
        # Altura mínima de la ventana.
        self.setMinimumHeight(500)
        
        # Texto de etiquetas.
        self.lbl_1.setText('Indicar el nombre del Apoyo para cada Nudo.')
        
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
        Acepta los cambios realizados en la QTableView y cierra el diálogo.
        """
        
        # Convierte en mayúsculas.
        col = 'Apoyo'
        self.df[col] = self.df[col].str.upper()
        
        # Cierra el diálogo.
        self.reject()
            
        print('\ndf_apoyos:')
        print(self.df)
