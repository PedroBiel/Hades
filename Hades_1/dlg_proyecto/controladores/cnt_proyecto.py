# -*- coding: utf-8 -*-
"""
CIERZO CTE DB SE-AE
Controlador de proyecto

Created on Thu Mar 2 13:45:00 2020

__author__ = Pedro Biel
__version__ = 1.0.0
__email__ = structural.eng.biel@gmail.com
"""


from dlg_proyecto.datos.iniciales_proyecto import DatosInicialesProyecto


class CntProyecto:
    """Controlador de los datos de proyecto."""
    
    def __init__(self, dialogo):
        self.d = dialogo
                
        # self.d.proyecto = DatosInicialesProyecto.PROYECTO

    def datos_iniciales_proyecto(self):
        
        proyecto = DatosInicialesProyecto.PROYECTO
        
        return proyecto
        
    def datos_proyecto(self):
        
        proyecto = self.d.lnt_proyecto.text()
        nombre = self.d.lnt_nombre.text()
        empresa = self.d.lnt_empresa.text()
        objeto = self.d.lnt_objeto.text()
        autor = self.d.lnt_autor.text()
        comentario = self.d.lnt_comentario.text()
        self.d.dcc_proyecto['proyecto'] = proyecto
        self.d.dcc_proyecto['nombre'] = nombre
        self.d.dcc_proyecto['empresa'] = empresa
        self.d.dcc_proyecto['objeto'] = objeto
        self.d.dcc_proyecto['autor'] = autor
        self.d.dcc_proyecto['comentario'] = comentario
        
        return self.d.dcc_proyecto
    