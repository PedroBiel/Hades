# -*- coding: utf-8 -*-
"""
DESCRIPCIÓN

Created on Wed Sep  9 14:27:24 2020

__author__ = Pedro Biel
__version__ = 0.0.0
__email__ = pbiel@taimweser.com
"""


from PyQt5 import uic
from PyQt5.QtWidgets import QAbstractScrollArea, QDialog

from dlg_grupos.controlador.cnt_grupos import CntGruposDialogo


class DlgGrupos(QDialog):
    
    def __init__(self, parent=None, model=None, df_grupos=None):
        """
        Diálog Grupos de la aplicación.
        
        Para pasar datos de QMainWindow a QDialog:
        https://stackoverflow.com/questions/14309703/passing-parameter-from-main-window-to-pop-up-qdialog-window
        """
        
        QDialog.__init__(self, parent)
        uic.loadUi('dlg_grupos/vista/dlg_grupos.ui', self)
        
        self.model = model
        
        self.df_grupos = df_grupos
        print('df_grupos:', self.df_grupos)
        
        # Widgets PyQt5.
        self.lbl_1 = self.label_1
        self.lbl_2 = self.label_2
        self.lbl_3 = self.label_3
        self.tbl = self.tableView
        self.btn_aceptar = self.pushButtonAceptar
        self.btn_rechazar = self.pushButtonRechazar
        self.btn_cerrar = self.pushButtonCerrar
        
        # Título de la ventana.
        self.setWindowTitle('Grupos')
        
        # Texto de etiquetas.
        self.lbl_1.setText(
            'Indicar Grupo para cada Caso y Nombre correspondiente.'
            )
        self.lbl_2.setText(
            'Casos y Nombres sin un Grupo asignado no se tendrán en cuenta.'
            )
        self.lbl_3.setText(
            'Modificaciones de los datos en Caso y Nombre pueden influir en el resultado final.'
            )
        
        # Modelo de la tabla.
        self.tbl.setModel(self.model)
        # Ajusta el ancho de las columnas a los contenidos.
        self.tbl.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tbl.resizeColumnsToContents()
        
        # Botones.
        self.btn_aceptar.setText('Aceptar cambios')
        self.btn_aceptar.setShortcut('Ctrl+A')
        self.btn_aceptar.setToolTip('Acepta los cambios en la tabla | Ctrl+A')
        
        self.btn_rechazar.setText('Rechazar cambios')
        self.btn_rechazar.setShortcut('Ctrl+R')
        self.btn_rechazar.setToolTip('Rechaza los cambios en la tabla | Ctrl+R')
        
        self.btn_cerrar.setText('Cerrar ventana')
        self.btn_cerrar.setShortcut('Ctrl+Q')
        self.btn_cerrar.setToolTip('Cierra la ventana | Ctrl+Q')
        self.btn_cerrar.clicked.connect(self.close)
        
        # Instancias de clase.
        self.cnt_grupos = CntGruposDialogo(self)
        
        # Eventos.
        self.btn_aceptar.clicked.connect(self.cnt_grupos.acepta_cambios)
