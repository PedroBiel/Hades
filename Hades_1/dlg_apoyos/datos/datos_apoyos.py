# -*- coding: utf-8 -*-
"""
Datos de los apoyos

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
    
    def __init__(self, pd, df_db):
        """
        Crea el DataFrame df_grupos donde obtener los grupos.

        Parameters
        ----------
        pd : pandas 
            Módulo pandas
        df_db : objeto pandas DataFrame
            Pandas DataFrame con los nudos originales de la base de datos.
        """
        
        self.pd = pd
        self.df_db = df_db
    
    def get_df(self):
        """
        Crea el DataFrame df donde asignar los apoyos.

        Returns
        -------
        df : objeto pandas DataFrame
            Pandas DataFrame con los apoyos.
        """
        
        df = self.pd.DataFrame()
        df['Nudo'] = self.df_db['Nudo'].unique()
        df['Apoyo'] = '--'
        
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
    
