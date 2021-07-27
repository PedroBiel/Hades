# -*- coding: utf-8 -*-
"""
Datos para las combinaciones de los DataFrames

Created on Wed Nov 18 09:58:29 2020

__author__ = Pedro Biel
__version__ = 0.0.0
__email__ = pbiel@taimweser.com
"""


class Combina2DF:
    """Combina (merge) los datos de dos DataFrames."""
    
    def __init__(self, pd):
        """
        pd  : librería pandas
        """
        
        self.pd = pd
        
    def merge_dataframes(self, df1, df2):
        """
        Combina los DataFrames df1 y df2 en un nuevo DataFrame df.
        
        df1 : pandas DataFrame
        df2 : pandas DataFrame
        
        return
        df : pandas DataFrame
        """
        
        df = self.pd.merge(df1, df2)
        
        return df


if __name__ == '__main__':

    import pandas as pd
    print(type(pd))
    
    d1 = {
        'caso': [100, 101, 200, 201, 300, 301, 400],
        'nombre': ['g1', 'g2', 'q1', 'q2', 'w1', 'w2', 'x']
        }
    d2 = {
        'nombre': ['g1', 'g2', 'q1', 'q2', 'w1', 'w2'],
        'grupo': ['G', 'G', 'Q', 'Q', 'W', 'W']
        }
    df1 = pd.DataFrame(d1)
    df2 = pd.DataFrame(d2)
    print(df1)
    print(df2)
    
    combina = Combina2DF(pd)
    df3 = combina.merge_dataframes(df1, df2)
    print(df3)
    print(type(df3))
