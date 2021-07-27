# -*- coding: utf-8 -*-
"""
CIERZO
Proyecto

Created on 14.04.2020

__author__ = Pedro Biel
__version__ = 1.0.0
__email__ = pbiel@taimweser.com
"""


from PyQt5 import uic
from PyQt5.QtWidgets import QDialog

from dlg_proyecto.controladores.cnt_proyecto import CntProyecto


class DlgProyecto(QDialog):
    
    def __init__(self, parent=None, d=None, model=None):
        
        QDialog.__init__(self, parent)
        uic.loadUi('vistas/dlg_proyecto.ui', self)
        
        self.d = d
        
        # Objetos de la aplicación.
        # =========================     
        # self.dcc_proyecto = {}  # Datos de proyecto
        
        # Instacnias de clases.
        # =====================
        self.cnt_proyecto = CntProyecto(self)
        
        # Objetos PyQt.
        # =============
        self.lnt_proyecto = self.lineEdit_proyecto
        self.lnt_nombre = self.lineEdit_nombre
        self.lnt_empresa = self.lineEdit_empresa
        self.lnt_objeto = self.lineEdit_objeto
        self.lnt_autor = self.lineEdit_autor
        self.lnt_comentario = self.lineEdit_comentario
        self.btn_aceptar = self.pushButton_aceptar
        self.btn_cancelar = self.pushButton_cancelar
        
        # Añade ítems a QLineEdit.
        # ========================
        if bool(self.d):  # d no vacio.
            self.dcc_proyecto = self.d.copy()
        else:  # d vacio.
            self.dcc_proyecto = self.cnt_proyecto.datos_iniciales_proyecto()
        
        self.lnt_proyecto.setText(self.dcc_proyecto['proyecto'])
        self.lnt_proyecto.selectAll()
        self.lnt_nombre.setText(self.dcc_proyecto['nombre'])
        self.lnt_empresa.setText(self.dcc_proyecto['empresa'])
        self.lnt_objeto.setText(self.dcc_proyecto['objeto'])
        self.lnt_autor.setText(self.dcc_proyecto['autor'])
        self.lnt_comentario.setText(self.dcc_proyecto['comentario'])
        
        # Eventos.
        # ========
        self.btn_aceptar.clicked.connect(self.cnt_proyecto.datos_proyecto)
        self.btn_aceptar.clicked.connect(self.reject)
        self.btn_cancelar.clicked.connect(self.close)

    def proyecto(self):
        
        return self.dcc_proyecto
    