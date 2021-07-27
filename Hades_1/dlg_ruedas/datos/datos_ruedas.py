# -*- coding: utf-8 -*-
"""
Datos de las ruedas

Created on Wed Sep 10 14:58 2020

__author__ = Pedro Biel
__version__ = 0.0.0
__email__ = structural.eng.biel@gmail.com
"""


class Unicos:
    """
    Crea un nuevo DataFrame con los valores únicos del DataFrame de la base de
    datos y les asigna el nº de ruedas.
    """
    
    def __init__(self, pd, df_apoyos):
        """
        Crea el DataFrame df_apoyos donde obtener los apoyos.

        Parameters
        ----------
        pd : pandas 
            Módulo pandas
        df_apoyos : objeto pandas DataFrame
            Pandas DataFrame con los nudos originales de la base de datos.
        """
        
        self.pd = pd
        self.df_apoyos = df_apoyos
    
    def get_df(self):
        """
        Crea el DataFrame df donde asignar los nº de ruedas.

        Returns
        -------
        df : objeto pandas DataFrame
            Pandas DataFrame con los nº de ruedas.
        """
        
        df = self.pd.DataFrame()
        df['Apoyo'] = self.df_apoyos['Apoyo'].unique()
        df.drop(df[df['Apoyo'] == '--'].index, inplace=True)
        df['Ruedas'] = 1
        
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
    
