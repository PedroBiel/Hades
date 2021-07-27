# -*- coding: utf-8 -*-
"""
Datos para converir DataFrame de pandas a diccionario de python

Created on Fri Feb 12 14:18:07 2021

__author__ = Pedro Biel
__version__ = 0.0.0
__email__ = pbiel@taimweser.com
"""


class DF2Dict:
    """Convierte DataFrame de pandas a diccionario de python."""
    
    def __init__(self, df):
        """Inicializa df."""
        
        self.df = df
        
    def df_columns(self):
        """Columnas del DataFrame."""
        
        return self.df.columns
    
    def diccionario(self):
        """Diccionario con los datos del DataFrame."""
        
        d = self.df.set_index('Grupo').to_dict()
        
        return d
    
    def relacion(self):
        """
        Obtiene de entre los subdiccionarios el diccionario con las relaciones.
        """
        
        d = self.diccionario()
        d_relacion = d['Relación']
        
        return d_relacion
    

if __name__ == '__main__':
    
    import pandas as pd
    
    d = {
        'Grupo': ['g', 'q', 'wx', 'wy'],
        'Relación': ['Y', 'YO', 'O', 'O'],
        'Mayoración': [1., 1., 1., 1.],
        'Redondeo': [1, 1, 1, 1]
        }
    df = pd.DataFrame(d)
    
    dicc = DF2Dict(df)
    print(dicc.df_columns())
    print(dicc.diccionario())
    print(dicc.relacion())