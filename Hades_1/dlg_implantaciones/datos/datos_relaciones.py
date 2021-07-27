# -*- coding: utf-8 -*-
"""
Datos para aplicar las relaciones

Created on Wed Nov 18 13:07:46 2020

__author__ = Pedro Biel
__version__ = 0.0.0
__email__ = pbiel@taimweser.com
"""


import pandas as pd
import numpy as np


class AplicaRelaciones:
    """Aplica las relaciones en un DataFrame."""
    
    def __init__(self, df_impl):
        """
        pd  : librería pandas
        df  : objeto pandas DataFrame.
        """
        
        self.df_impl = df_impl
        
    def reordena_columnas(self):
        """
        Reordena las columnas y renombra las columnas de los esfuerzos.
        
        Return
        ------
        df : objeto pandas DataFrame
        """
        
        df = pd.DataFrame()
        df['Modelo'] = self.df_impl['Modelo']
        df['Nudo'] = self.df_impl['Nudo']
        df['Caso'] = self.df_impl['Caso']
        df['Grupo'] = self.df_impl['Grupo']
        df['Relación'] = self.df_impl['Relación']
        df['Mayoración'] = self.df_impl['Mayoración']
        df['Redondeo'] = self.df_impl['Redondeo']
        df['Apoyo'] = self.df_impl['Apoyo']
        df['Ruedas'] = self.df_impl['Ruedas']
        df['V'] = self.df_impl['Fz']
        df['Hx'] = self.df_impl['Fx']
        df['Hy'] = self.df_impl['Fy']
        df['Mz'] = self.df_impl['Mz']
        df['Mx'] = self.df_impl['Mx']
        df['My'] = self.df_impl['My']
        
        df['signo_V'] = self.df_impl['signo_Fz']
        df['signo_Hx'] = self.df_impl['signo_Fx']
        df['signo_Hy'] = self.df_impl['signo_Fy']
        df['signo_Mz'] = self.df_impl['signo_Mz']
        df['signo_Mx'] = self.df_impl['signo_Mx']
        df['signo_My'] = self.df_impl['signo_My']

        return df
    
    def multiplica_signos(self):
        """
        Multiplica las reacciones por los signos.
        
        Return
        ------
        df : objeto pandas DataFrame
        """
        
        df = self.df_impl.copy()
        df['V'] *= df['signo_V']
        df['Hx'] *= df['signo_Hx']
        df['Hy'] *= df['signo_Hy']
        df['Mz'] *= df['signo_Mz']
        df['Mx'] *= df['signo_Mx']
        df['My'] *= df['signo_My']
        
        cols = [
            'Modelo', 'Nudo', 'Caso', 'Grupo', 'Relación', 'Mayoración',
            'Redondeo', 'Apoyo', 'Ruedas', 'V', 'Hx', 'Hy', 'Mz', 'Mx', 'My'
            ]
        
        return df[cols]
    
    def divide_ruedas(self):
        """
        Divide las reacciones por el número de ruedas en el apoyo.

        Returns
        -------
        df : objeto pandas DataFrame
        """
        
        df = self.df_impl.copy()
        cols = ('V', 'Hx', 'Hy', 'Mx', 'My', 'Mz')
        for col in cols:
            df[col] = df[col] / df['Ruedas']
        
        return df
    
    def mayora_cargas(self):
        """
        Mayora las cargas por el coeficiente de mayoración

        Returns
        -------
        df : objeto pandas DataFrame
        """
        
        df = self.df_impl.copy()
        cols = ('V', 'Hx', 'Hy', 'Mx', 'My', 'Mz')
        for col in cols:
            df[col] = df[col] * df['Mayoración'].astype('float')
        
        return df

    def redondea_cargas(self):
        """
        Mayora las cargas por el coeficiente de mayoración

        Returns
        -------
        df : objeto pandas DataFrame
        """
        
        df = self.df_impl.copy()
        cols = ('V', 'Hx', 'Hy', 'Mx', 'My', 'Mz')
        for col in cols:
            df[col] = df[col] / df['Redondeo'].astype('float')
            df[col] = df[col].apply(np.ceil)
            df[col] = df[col] * df['Redondeo'].astype('float')
            df[col] = df[col].astype(int)
        
        cols = [
            'Modelo', 'Nudo', 'Caso', 'Grupo', 'Relación', 'Apoyo', 'Ruedas', 
            'V', 'Hx', 'Hy', 'Mz', 'Mx', 'My'
            ]
            
        return df

