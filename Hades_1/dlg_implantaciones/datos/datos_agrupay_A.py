# -*- coding: utf-8 -*-
"""
Datos para agrupar el DataFrame aplicando la relación 'y'

Created on Fri Dec  4 11:48:22 2020

__author__ = Pedro Biel
__version__ = 0.0.0
__email__ = pbiel@taimweser.com
"""


class AgrupaY:
    """Agrupa el DataFrame aplicando la relación 'y'."""
    
    def __init__(self, df_implantaciones):
        """Inicializa df_implantaciones."""

        self.df_implantaciones = df_implantaciones
        
        self.cols = ['V', 'Hx', 'Hy', 'Mx', 'My', 'Mz']
        self.idxs = ['Modelo', 'Apoyo', 'Grupo', 'Relación']
        
    def dataframe_gropuby_sum(self, df):
        """
        Agrupa df aplicando la suma.

        Returns
        -------
        df_sum : pandas DataFrame
        """
        
        df_sum = df.groupby(self.idxs)[self.cols].sum()
        
        return df_sum
    
    def dataframe_y(self, level, modelo):
        """
        Agrupa un DataFrame por máximos y mínimos.

        Parameters
        ----------
        level  : lista de str ; nivel de los índices del DataFrame agrupado
        modelo : bool         ; True -> se indica el modelo en columnas;
                                False -> no se indica el modelo en las 
                                columnas.

        Returns
        -------
        df_y : pandas DataFrame
        """
        
        df_sum = self.dataframe_gropuby_sum(self.df_implantaciones)
        
        if modelo:
            df_y = df_sum.groupby(level=level).agg([
                ('max', max),
                ('Modelo_max', lambda x: x.idxmax()[0]),
                ('min', min),
                ('Modelo_min', lambda x: x.idxmin()[0])
                ])
        else:
             df_y = df_sum.groupby(level=level).agg(['max', 'min'])
        
        return df_y
    
    
        
        