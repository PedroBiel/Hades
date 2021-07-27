# -*- coding: utf-8 -*-
"""
Datos de los signos de las cargas

Created on Wed Oct 21 12:50 2020

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
        Crea el DataFrame df donde asignar los signos.

        Returns
        -------
        df : objeto pandas DataFrame
            Pandas DataFrame con las relaciones.
        """
        
        df = self.pd.DataFrame()
        df['Grupo'] = self.df_grupos['Grupo'].unique()
        df.drop(df[df['Grupo'] == '--'].index, inplace=True)
        df['signo_Fx'] = -1
        df['signo_Fy'] = -1
        df['signo_Fz'] = 1
        df['signo_Mx'] = -1
        df['signo_My'] = -1
        df['signo_Mz'] = 1
        
        return df


class Signos:
    """Crea un nuevo DataFrame con los valores de los signos de las cargas."""
    
    def __init__(self, pd):
        """
        Crea el DataFrame df_db donde obtener los signos de las cargas.
        
        Parameters
        ----------
        pd : pandas 
            Módulo pandas
        """
        
        self.pd = pd
    
    def get_df(self):
        """
        Crea el DataFrame df donde asignar los signos.

        Returns
        -------
        df : objeto pandas DataFrame
            Pandas DataFrame con los signos.
        """

        d = {
            'signo_Fx': [-1],
            'signo_Fy': [-1],
            'signo_Fz': [1],
            'signo_Mx': [-1],
            'signo_My': [-1],
            'signo_Mz': [1],
            }
        df = self.pd.DataFrame(d)

        return df


if __name__ == '__main__':

    # Debbuging según MITx.
    
    import pandas as pd
    
    # Crea pandas DataFrame df.
    signos = Signos(pd)
    df = signos.get_df()
    print(df)
