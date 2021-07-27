# -*- coding: utf-8 -*-
"""
Datos de los grupos

Created on Wed Sep 10 14:58 2020

__author__ = Pedro Biel
__version__ = 0.0.0
__email__ = structural.eng.biel@gmail.com
"""


class Unicos:
    """
    Crea un nuevo DataFrame con los valores únicos del DataFrame de la base de
    datos y les asigna el grupo.
    """
    
    def __init__(self, pd, df_db):
        """
        Crea el DataFrame df_db donde obtener los casos y los nombres.

        Parameters
        ----------
        pd : pandas 
            Módulo pandas
        df_db : objeto pandas DataFrame
            Pandas DataFrame con los casos y nombre originales de la base de 
            datos.
        """
        
        self.pd = pd
        self.df_db = df_db
    
    def get_df(self):
        """
        Crea el DataFrame df donde asignar los grupos.
        Los valores de las columnas Caso y Nombre están relacionados, a 
        cada caso corresponde un único nombre.

        Returns
        -------
        df : objeto pandas DataFrame
            Pandas DataFrame con los grupos.
        """
        
        # print('\n unicos = Unicos(self.v.pd, self.v.df_db)')
        
        df = self.pd.DataFrame()
        df['Caso'] = self.df_db['Caso'].unique()
        df['Nombre'] = self.df_db['Nombre'].unique()
        df['Grupo'] = '--'
        
        return df


if __name__ == '__main__':

    # Debbuging según MITx.
    
    import pandas as pd
    
    # Crea pandas DataFrame df.
    d = {
        'Caso': ['a', 'b', 'b', 'c', 'a', 'd'],
        'Nombre': [1, 2, 2, 3, 1, 4]
        }
    df = pd.DataFrame(d)
    print(df)
    
    # Crea pandas DataFrame con únicos de df.
    unicos = Unicos(pd, df)
    df_unicos = unicos.get_df()
    print(df_unicos)
    
    # Prueba que los DataFrames son independientes.
    df_unicos['Caso'] = 'x'
    print(df_unicos)
    print(df)
    
