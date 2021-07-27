# -*- coding: utf-8 -*-
"""
Datos de los coeficientes de mayoración y redondeos

Created on Fri Nov 13 13:37 2020

__author__ = Pedro Biel
__version__ = 0.0.0
__email__ = structural.eng.biel@gmail.com
"""


class Unicos:
    """
    Crea un nuevo DataFrame con los valores únicos del DataFrame de la base de
    datos y les asigna los coeficientes de mayoración y redondeos.
    """
    
    def __init__(self, pd, df_grupos):
        """
        Crea el DataFrame df_grupos donde obtener los apoyos.

        Parameters
        ----------
        pd : pandas 
            Módulo pandas
        df_grupos : objeto pandas DataFrame
            Pandas DataFrame con los nudos originales de la base de datos.
        """
        
        self.pd = pd
        self.df_grupos = df_grupos
    
    def get_df(self):
        """
        Crea el DataFrame df donde asignar los coeficientes y redondeos.

        Returns
        -------
        df : objeto pandas DataFrame
            Pandas DataFrame con los nº de ruedas.
        """
        
        df = self.pd.DataFrame()
        df['Grupo'] = self.df_grupos['Grupo'].unique()
        df.drop(df[df['Grupo'] == '--'].index, inplace=True)
        df['Mayoración'] = 1.0
        df['Redondeo'] = 1
        
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
    
