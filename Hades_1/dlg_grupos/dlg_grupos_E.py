# -*- coding: utf-8 -*-
"""
HADES
Diálogo Grupos

Created on Wed Sep  9 14:27:24 2020

__author__ = Pedro Biel
__version__ = 0.0.0
__email__ = pbiel@taimweser.com
"""


from PyQt5 import uic
from PyQt5.QtWidgets import QAbstractScrollArea, QDialog

from dlg_grupos.controlador.cnt_grupos import CntGruposDialogo
from dlg_grupos.modelo.mdl_tablemodeleditable import PandasModelEditable



class DlgGrupos(QDialog):
    
    def __init__(self, parent=None, df=None):
        """
        Diálogo Grupos de la aplicación.
        
        Para pasar datos de QMainWindow a QDialog:
        https://stackoverflow.com/questions/14309703/passing-parameter-from-main-window-to-pop-up-qdialog-window
        """
        
        QDialog.__init__(self, parent)
        uic.loadUi('dlg_grupos/vista/dlg_grupos.ui', self)
        
        self.df = df
        
        # Widgets PyQt5.
        self.lbl_1 = self.label_1
        self.lbl_2 = self.label_2
        self.lbl_3 = self.label_3
        self.tbl = self.tableView
        self.btn_aceptar = self.pushButtonAceptar
        
        # Título de la ventana.
        self.setWindowTitle('Grupos')
        
        # Altura mínima de la ventana.
        self.setMinimumHeight(500)
        
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
        self.model = PandasModelEditable(self.df)
        self.tbl.setModel(self.model)
        # Ajusta el ancho de las columnas a los contenidos.
        self.tbl.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tbl.resizeColumnsToContents()
        
        # Botones.
        self.btn_aceptar.setText('Aceptar cambios')
        self.btn_aceptar.setShortcut('Ctrl+A')
        self.btn_aceptar.setToolTip('Acepta los cambios en la tabla | Ctrl+A')
        
        # Instancias de clase.
        self.cnt_grupos = CntGruposDialogo(self)
        
        # Eventos.
        self.btn_aceptar.clicked.connect(self.acepta_cambios)
        
    def acepta_cambios(self):
        """
        Acepta los cambios realizados en la QTableView y cierra el diálogo.
        """
    
        self.df = self.cnt_grupos.tablemodel_df()
        self.reject()
        
        return self.df
        
    # def rechaza_cambios(self):
    #     """
    #     Rechaza los cambios realizados en la QTableView y cierra el diálogo.
    #     """
        
    #     self.tbl.setModel(self.model)
    
    def get_df(self):
        """Getter del DataFrame modificado."""
       
        self.df = self.acepta_cambios()

        return self.df
