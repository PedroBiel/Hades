# -*- coding: utf-8 -*-
"""
Datos para agrupar el DataFrame aplicando la relación 'o'

Created on Mon Feb  1 14:54:29 2021

__author__ = Pedro Biel
__version__ = 0.0.0
__email__ = pbiel@taimweser.com
"""


class AgrupaO:
    """Agrupa el DataFrame aplicando la relación 'o'."""
    
    def __init__(self, df_implantaciones):
        """Inicializa df_implantaciones."""

        self.df_implantaciones = df_implantaciones
        
        self.cols = ['V', 'Hx', 'Hy', 'Mx', 'My', 'Mz']
        self.idxs = ['Modelo', 'Apoyo', 'Nudo', 'Grupo', 'Caso', 'Relación']
    
    def dataframe_gropuby_sum_max_min(self, df):
        """
        Agrupa df aplicando la suma.

        Returns
        -------
        df_sum : pandas DataFrame
        """
        
        df_sum_max_min = df.groupby(self.idxs)[self.cols].sum()
        
        return df_sum_max_min
    
    def dataframe_o(self, level, modelo):
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
        df_o : pandas DataFrame
        """
        
        df_sum_max_min = self.dataframe_gropuby_sum_max_min(
            self.df_implantaciones
            )
        
        if modelo:
            df_o = df_sum_max_min.groupby(level=level).agg([
                ('max', max),
                ('Modelo_max', lambda x: x.idxmax()[0]),
                ('min', min),
                ('Modelo_min', lambda x: x.idxmin()[0])
                ])
        else:
            df_o = df_sum_max_min.groupby(level=level).agg(['max', 'min'])
        
        return df_o
    