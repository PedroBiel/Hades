# -*- coding: utf-8 -*-
"""
HADES
Salidas del diálogo de fichero

Created on Mon Aug  3 14:17:53 2020

__author__ = Pedro Biel
__version__ = 0.0.0
__email__ = pbiel@taimweser.com
"""


class SalidasDlgFichero:
    
    def __init_(self, ventana):
        
        self.v = ventana
        
    def status_bar(self, text):
        """Texto informativo en status bar."""
        
        self.statusbar.setFont(QFont('Consolas', 8))
        self.statusbar.showMessage(text)
        
    
    def salida_ruta_nombre_db(self):
        """Salida de la ruta y el nombre de la base de satos."""
        
        self.v.lbl_db.setText(self.ruta_nombre_db)
        self.v.lbl_dimensiones.setText(self.df_db_shape)
        self.v.lbl_tiempo.setText(self.df_db_tiempo)
