# -*- coding: utf-8 -*-
"""
Datos del diálogo de fichero

Created on Mon Aug  3 14:47:46 2020

__author__ = Pedro Biel
__version__ = 0.0.0
__email__ = pbiel@taimweser.com
"""


class ConvierteTiposDF():
    
    def __init__(self, df):
        """
        Crea el DataFrame df.

        Returns
        -------
        df : astype -> desconocido
        """
        
        self.df = df
    
    def tipo_valores(self):
        """
        Convierte el tipo de datos de las columnas del Dataframe.

        Returns
        -------
        df : objeto pandas DataFrame
        """
        
        self.df['Nudo'] = self.df['Nudo'].astype(str)
        self.df['Caso'] = self.df['Caso'].astype(str)
        cols = ['Fx', 'Fy', 'Fz', 'Mx', 'My', 'Mz']
        for col in cols:
            try:
                self.df[col] = self.df[col].replace(',', '.').astype(float)
                self.df[col] = self.df[col].replace(0, 0.0).astype(float)
                self.df[col].fillna(0.0, inplace=True)
            except:
                self.df[col] = self.df[col].str.replace(',', '.').astype(float)
                self.df[col].fillna(0.0, inplace=True)
                
        return self.df