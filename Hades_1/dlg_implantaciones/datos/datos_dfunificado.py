# -*- coding: utf-8 -*-
"""
DESCRIPCIÓN

Created on Fri Feb 12 14:35:12 2021

__author__ = Pedro Biel
__version__ = 0.0.0
__email__ = pbiel@taimweser.com
"""


class DFUnificado:
    """
    DataFrame unificado con los DataFrames Y, YO y O según las relaciones
    """
    
    def __init__(self):
        """
        Inicializa los DataFrames

        Returns
        -------
        df_unificado : pandas DataFrame ; valores unificados según la relación
                                          del grupo.
        """
        
    def reinicia_indidice(self, df):
        """Reinicia el índice del DataFrame."""
        
        return df.reset_index()
    
    def unifica(self, df_y, df_yo, df_o, d_relacion, level):
        """
        Unifica DataFrames.
        
        Parameters
        ----------
        df_y  : pandas DataFrame ; valores con la relación Y (suma de los 
                                   valore del grupo).                                                             grupo).
        df_yo : pandas DataFrame ; valores con la relación YO (suma de los
                                   valores positivos y de los valores 
                                   negativos del grupo).
        df_o  : pandas DataFrame ; valores máximos positivos y mínimos 
                                   negativos del grupo).
        d_relacion : dict ; diccionario con las relaciones.
        level : str list         ; lista con los niveles del índice. 
        """
        
        df_y_reset_idx = self.reinicia_indidice(df_y)
        df_yo_reset_idx = self.reinicia_indidice(df_yo)
        df_o_reset_idx = self.reinicia_indidice(df_o)
        
        df = df_y_reset_idx.copy()
        for grupo in d_relacion.keys():
            if (d_relacion[grupo] == 'Y') or (d_relacion[grupo] == 'y'):
                df = df.where(df['Grupo'] != grupo, df_y_reset_idx)
            elif (d_relacion[grupo] == 'YO') or (d_relacion[grupo] == 'yo'):
                df = df.where(df['Grupo'] != grupo, df_yo_reset_idx)
            elif (d_relacion[grupo] == 'O') or (d_relacion[grupo] == 'o'):
                df = df.where(df['Grupo'] != grupo, df_o_reset_idx)

        df.set_index(level, inplace=True)
        
        return df
    