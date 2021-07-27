# -*- coding: utf-8 -*-
"""
Datos de las relaciones

Created on Fri Oct 2 13:24 2020

__author__ = Pedro Biel
__version__ = 0.0.0
__email__ = structural.eng.biel@gmail.com
"""


class Unicos:
    """
    Crea un nuevo DataFrame con los valores únicos del DataFrame de la base de
    datos y les asigna la relación.
    """
    
    def __init__(self, pd, df_grupos):
        """
        Crea el DataFrame df_grupos donde obtener los grupos.

        Parameters
        ----------
        pd : pandas 
            Módulo pandas
        df_grupos : objeto pandas DataFrame
            Pandas DataFrame con los grupos.
        """
        
        self.pd = pd
        self.df_grupos = df_grupos
    
    def get_df(self):
        """
        Crea el DataFrame df donde asignar las relaciones.
        Los valores de las columnas Caso y Nombre están relacionados, a 
        cada caso corresponde un único nombre.

        Returns
        -------
        df : objeto pandas DataFrame
            Pandas DataFrame con las relaciones.
        """
        
        df = self.pd.DataFrame()
        df['Grupo'] = self.df_grupos['Grupo'].unique()
        df.drop(df[df['Grupo'] == '--'].index, inplace=True)
        df['Relación'] = 'Y'
        df['Mayoración'] = 1.0
        df['Redondeo'] = 1
        
        return df



if __name__ == '__main__':

    # Debbuging según MITx.
    
    import pandas as pd
    
    # Crea pandas DataFrame df.
    d = {'Grupo': ['G', 'G', 'Q', '--', 'Wy', '--'],}
    df = pd.DataFrame(d)
    print(df)
    
    # Crea pandas DataFrame con únicos de df.
    unicos = Unicos(pd, df)
    df_unicos = unicos.get_df()
    print(df_unicos)
    
    # Prueba que los DataFrames son independientes.
    df_unicos['Grupo'] = 'x'
    print(df_unicos)
    print(df)
    
