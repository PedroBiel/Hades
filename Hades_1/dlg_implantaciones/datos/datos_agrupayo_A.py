# -*- coding: utf-8 -*-
"""
Datos para agrupar el DataFrame aplicando la relación 'yo'

Created on Mon Feb  8 11:42:18 2021

__author__ = Pedro Biel
__version__ = 0.0.0
__email__ = pbiel@taimweser.com
"""


class AgrupaYO:
    """Agrupa el DataFrame aplicando la relación 'yo'."""
    
    def __init__(self, df_implantaciones, pd):
        """Inicializa df_implantaciones."""

        self.df_implantaciones = df_implantaciones
        self.pd = pd
        
        self.cols = ['V', 'Hx', 'Hy', 'Mx', 'My', 'Mz']
        self.idxs = ['Modelo', 'Apoyo', 'Grupo']
    
    def dataframe_groupby_agg_sum(self, df):
        """
        Agrupa df agregando la suma de los valores positivos y la suma de los 
        valores negativos.

        Returns
        -------
        df_agg_sum : pandas DataFrame
        """
        
        df_sum = df.groupby(self.idxs)[self.cols].agg([
            ('max', lambda x: x[x >= 0].sum()),
            ('min', lambda x: x[x < 0].sum())
            ])
            
        return df_sum
    
    def multi_indice(self, modelo):
        """Crea multiíndice para el cabecero del DataFrame."""
        
        if modelo:
            multi_ind = self.pd.DataFrame(
                columns=self.pd.MultiIndex.from_product([
                    self.cols,
                    ('max', 'Modelo_max', 'min', 'Modelo_min')
                    ]))
        else:
            multi_ind = self.pd.DataFrame(
                columns=self.pd.MultiIndex.from_product([
                    self.cols,
                    ('max', 'min')
                    ]))
        
        return multi_ind
    
    def model_minmax_opt(self, gr, modelo):
        """
        https://stackoverflow.com/questions/65701989/get-sum-of-positive-values-and-sum-of-negative-values
        """
        
        multi_ind = self.multi_indice(modelo)
        
        # start with a deep copy of the result template
        tf = multi_ind.copy(deep=True)
        
        if modelo:
            for val in self.cols:
                max_pos = gr[(val, 'sum_pos')].idxmax()
                min_neg = gr[(val, 'sum_neg')].idxmin()
                tf.loc[0, [(val, 'max'), (val, 'Modelo_max')]] = gr.loc[
                    max_pos, [(val, 'sum_pos'), ('Modelo', '')]
                    ].values
                tf.loc[0, [(val, 'min'), (val, 'Modelo_min')]] = gr.loc[
                    min_neg, [(val, 'sum_neg'), ('Modelo', '')]
                    ].values
        else:
            for val in self.cols:
                max_pos = gr[(val, 'sum_pos')].idxmax()
                min_neg = gr[(val, 'sum_neg')].idxmin()
                tf.loc[0, [(val, 'max')]] = gr.loc[max_pos, [(val, 'sum_pos')]
                    ].values
                tf.loc[0, [(val, 'min')]] = gr.loc[min_neg, [(val, 'sum_neg')]
                    ].values
        
        return tf
    
    def dataframe_yo(self, level, modelo):
        """
        Agrupa yn DataFrame por máximos y mínimos.

        Parameters
        ----------
        level  : lista de str ; nivel de los índices del DataFrame agrupado
        modelo : bool         ; True -> se indica el modelo en columnas;
                                False -> no se indica el modelo en las 
                                columnas.

        Returns
        -------
        df_yo : pandas DataFrame
        """
        
        def model_minmax_opt_1(gr):
            multi_ind = self.multi_indice(modelo)
            tf = multi_ind.copy(deep=True)
            for val in self.cols:
                max_pos = gr[(val, 'max')].idxmax()
                min_neg = gr[(val, 'min')].idxmin()
                tf.loc[0, [(val, 'max'), (val, 'Modelo_max')]] = gr.loc[
                    max_pos, [(val, 'max'), ('Modelo', '')]
                    ].values
                tf.loc[0, [(val, 'min'), (val, 'Modelo_min')]] = gr.loc[
                    min_neg, [(val, 'min'), ('Modelo', '')]
                    ].values
                
            return tf
        
        def model_minmax_opt_2(gr):
            multi_ind = self.multi_indice(modelo)
            tf = multi_ind.copy(deep=True)
            for val in self.cols:
                max_pos = gr[(val, 'max')].idxmax()
                min_neg = gr[(val, 'min')].idxmin()
                tf.loc[0, [(val, 'max')]] = gr.loc[max_pos, [(val, 'max')]
                    ].values
                tf.loc[0, [(val, 'min')]] = gr.loc[min_neg, [(val, 'min')]
                    ].values
                
            return tf
        
        df_sum = self.dataframe_groupby_agg_sum(self.df_implantaciones)
        group = df_sum.reset_index().groupby(level)
        if modelo:
            df_yo = group.apply(model_minmax_opt_1)
        else:
            df_yo = group.apply(model_minmax_opt_2)
        
        # get rid of the added 0-index
        df_yo.reset_index(level=2, drop=True, inplace=True)

        return df_yo
        
        
        