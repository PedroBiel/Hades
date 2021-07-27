# -*- coding: utf-8 -*-
"""
Controlador de las implantaciones

Created on Wed Nov 18 09:25:56 2020

__author__ = Pedro Biel
__version__ = 0.0.0
__email__ = pbiel@taimweser.com
"""


from dlg_implantaciones.datos.datos_combinadf import Combina2DF
from dlg_implantaciones.datos.datos_creadf import CreaDF
from dlg_implantaciones.datos.datos_agrupay import AgrupaY
from dlg_implantaciones.datos.datos_agrupao import AgrupaO
from dlg_implantaciones.datos.datos_agrupayo import AgrupaYO
from dlg_implantaciones.datos.datos_dfadict import DF2Dict
from dlg_implantaciones.datos.datos_dfunificado import DFUnificado


class CntImplantaciones:
    """Controlador de las implantaciones."""
    
    def __init__(self, ventana):
        """Crea la ventana de MainWindow."""
        
        self.v = ventana
        
        self.t0 = ''
        self.t1 = ''
        
    def get_pandas(self):
        """Getter de la librería pandas."""
        
        return self.v.pd
        
    def get_dataframe_db(self):
        """Getter del DataFrame df_db."""
        
        return self.v.df_db.copy()
    
    def get_dataframe_grupos(self):
        """Getter del DataFrame df_grupos."""
        
        return self.v.df_grupos.copy()
    
    def get_dataframe_relaciones(self):
        """Getter del DataFrame df_.relaciones"""
        
        return self.v.df_relaciones.copy()
    
    def get_dataframe_apoyos(self):
        """Getter del DataFrame df_apoyos."""
        
        return self.v.df_apoyos.copy()
    
    def get_dataframe_ruedas(self):
        """Getter del DataFrame df_ruedas."""
        
        return self.v.df_ruedas.copy()
    
    def get_dataframe_signos(self):
        """Getter del DataFrame df_signos."""
        
        return self.v.df_signos.copy()
        
    def get_dataframe_implantaciones(self):
        """Getter del DataFrame df_implantaciones."""
        
        return self.v.df_implantaciones.copy()
    
    def set_dataframe_implantaciones(self, df_impl):
        """Setter del DataFrame df_implantaciones."""
        
        self.v.df_implantaciones = df_impl.copy()
        
    def get_dataframe_implantaciones_ap_gr(self):
        """Getter del DataFrame df_impl_ap_gr."""
        
        return self.v.df_impl_ap_gr.copy()
    
    def set_dataframe_implantaciones_ap_gr(self, df_impl):
        """Setter del DataFrame df_impl_ap_gr."""
        
        self.v.df_impl_ap_gr = df_impl.copy()
        
    def get_dataframe_implantaciones_ap_gr_modelo(self):
        """Getter del DataFrame df_impl_ap_gr_modelo."""
        
        return self.v.df_impl_ap_gr_modelo.copy()
    
    def set_dataframe_implantaciones_ap_gr_modelo(self, df_impl):
        """Setter del DataFrame df_impl_ap_gr_modelo."""
        
        self.v.df_impl_ap_gr_modelo = df_impl.copy()
           
    def get_dataframe_implantaciones_gr_ap(self):
        """Getter del DataFrame df_impl_gr_ap."""
        
        return self.v.df_impl_gr_ap.copy()
    
    def set_dataframe_implantaciones_gr_ap(self, df_impl):
        """Setter del DataFrame df_impl_gr_ap."""
        
        self.v.df_impl_gr_ap = df_impl.copy()
        
    def get_dataframe_implantaciones_gr_ap_modelo(self):
        """Getter del DataFrame df_impl_gr_ap_modelo."""
        
        return self.v.df_impl_gr_ap_modelo.copy()
    
    def set_dataframe_implantaciones_gr_ap_modelo(self, df_impl):
        """Setter del DataFrame df_impl_gr_ap_modelo."""
        
        self.v.df_impl_gr_ap_modelo = df_impl.copy()    
        
    def crea_implantaciones(self):
        """
        Crea el DataFrame de implantaciones df_implantaciones a partir de los 
        DataFrames creados en los dialogos (df_db, df_grupos, df_relaciones, 
        df_apoyos, df_ruedas, df_signos).
        """

        self.pd = self.get_pandas()
        
        # Status bar.
        text = 'Creando tablas para los cuadros de implantación...'
        self.v.status_bar(text)
        
        # Inicia cronómetro.
        #self.t0 = self.v.time.clock()
        self.t0 = self.v.time.perf_counter()
        
        try:
            # 1. Crea el DataFrame.
            df_impl = self.crea_dataframe()
            # print('\ndf_impl 1')
            # print(df_impl)
            # print(df_impl.dtypes)
            # print(df_impl.describe().T)
            crea_df = CreaDF()
            df_impl = crea_df.reordena_columnas(df_impl)
            df_impl = crea_df.multiplica_signos(df_impl)
            df_impl = crea_df.divide_ruedas(df_impl)
            df_impl = crea_df.mayora_cargas(df_impl)
            df_impl = crea_df.redondea_cargas(df_impl)  # TODO ¿Redondear al final?
            # print('\ndf_impl 3')
            # print(df_impl)
            # print(df_impl.dtypes)
            # print(df_impl.describe().T)
            
        except KeyError as e:
            print('KeyError:', e)
            print('\ncrea_implantaciones.df_implantaciones')
            print(self.v.df_implantaciones)  #TODO cuando se abre un proyecto existe este df.
            df_impl = self.v.df_implantaciones.copy()
            
        self.set_dataframe_implantaciones(df_impl)
            
        # 2. DataFrame agrupado por relaciones 'y'.
        level_ap_gr = ['Apoyo', 'Grupo']
        level_gr_ap = ['Grupo', 'Apoyo']
        agrupa_y = AgrupaY(df_impl)
        df_y_ap_gr = agrupa_y.dataframe_y(level_ap_gr, modelo=False)
        df_y_ap_gr_modelo = agrupa_y.dataframe_y(level_ap_gr, modelo=True)
        df_y_gr_ap = agrupa_y.dataframe_y(level_gr_ap, modelo=False)
        df_y_gr_ap_modelo = agrupa_y.dataframe_y(level_gr_ap, modelo=True)
        # print('\ndf_y_ap_gr')
        # print(df_y_ap_gr)
        # print('\ndf_y_ap_gr_modelo')
        # print(df_y_ap_gr_modelo)
        # print('\ndf_y_gr_ap')
        # print(df_y_gr_ap)
        
        # 3. DataFrame agrupado por relaciones 'o'.
        agrupa_o = AgrupaO(df_impl)
        df_o_ap_gr = agrupa_o.dataframe_o(level_ap_gr, modelo=False)
        df_o_ap_gr_modelo = agrupa_o.dataframe_o(level_ap_gr, modelo=True)
        df_o_gr_ap = agrupa_o.dataframe_o(level_gr_ap, modelo=False)
        df_o_gr_ap_modelo = agrupa_o.dataframe_o(level_gr_ap, modelo=True)
        # print('\ndf_o_ap_gr')
        # print(df_o_ap_gr)
        # print('\ndf_o_ap_gr_modelo')
        # print(df_o_ap_gr_modelo)
        # print('\ndf_o_gr_ap')
        # print(df_o_gr_ap)
        
        # 4. DataFrame agrupado por relaciones 'yo'.
        agrupa_yo = AgrupaYO(df_impl, self.pd)
        df_yo_ap_gr = agrupa_yo.dataframe_yo(level_ap_gr, modelo=False)
        df_yo_ap_gr_modelo = agrupa_yo.dataframe_yo(level_ap_gr, modelo=True)
        df_yo_gr_ap = agrupa_yo.dataframe_yo(level_gr_ap, modelo=False)
        df_yo_gr_ap_modelo = agrupa_yo.dataframe_yo(level_gr_ap, modelo=True)
        # print('\ndf_yo_ap_gr')
        # print(df_yo_ap_gr)
        # print('\ndf_yo_ap_gr_modelo')
        # print(df_yo_ap_gr_modelo)
        # print('\ndf_yo_gr_ap')
        # print(df_yo_gr_ap)
        
        # 5. DataFrame unificada según las relaciones de cada grupo.
        # 5.1 Diccionario con las relaciones.
        df_relaciones = self.get_dataframe_relaciones()
        dicc = DF2Dict(df_relaciones)
        d_relacion = dicc.relacion()
        # 5.2 DataFrame unificada.
        df_unificado = DFUnificado()
        df_ap_gr = df_unificado.unifica(
            df_y_ap_gr, 
            df_yo_ap_gr, 
            df_o_ap_gr, 
            d_relacion, 
            level_ap_gr
            )
        df_ap_gr_modelo = df_unificado.unifica(
            df_y_ap_gr_modelo, 
            df_yo_ap_gr_modelo, 
            df_o_ap_gr_modelo, 
            d_relacion, 
            level_ap_gr
            )
        df_gr_ap = df_unificado.unifica(
            df_y_gr_ap, 
            df_yo_gr_ap, 
            df_o_gr_ap, 
            d_relacion, 
            level_gr_ap
            )
        df_gr_ap_modelo = df_unificado.unifica(
            df_y_gr_ap_modelo, 
            df_yo_gr_ap_modelo, 
            df_o_gr_ap_modelo, 
            d_relacion, 
            level_gr_ap
            )
        
        self.set_dataframe_implantaciones_ap_gr(df_ap_gr)
        self.set_dataframe_implantaciones_ap_gr_modelo(df_ap_gr_modelo)
        self.set_dataframe_implantaciones_gr_ap(df_gr_ap)
        self.set_dataframe_implantaciones_gr_ap_modelo(df_gr_ap_modelo)
        
        print('\ncrea_implantaciones.df_impl_ap_gr_modelo')
        print(self.v.df_impl_ap_gr_modelo)
            
        # Cronometra.
        #self.t1 = self.v.time.clock()
        self.t1 = self.v.time.perf_counter()
        t = self.t1 - self.t0
        self.v.xlsx_tiempo = t
        
    def crea_dataframe(self):
        """
        Crea el DataFrame de implantaciones df_implantaciones a partir de 
        los DataFrames creados en los dialogos (df_db, df_grupos, 
        df_relaciones, df_apoyos, df_ruedas, df_signos).

        Returns
        -------
        df : objeto pandas DataFrame
            Pandas DataFrame con los datos de las implantaciones.
        """
        
        df_db = self.get_dataframe_db()
        df_grupos = self.get_dataframe_grupos()
        df_relaciones = self.get_dataframe_relaciones()
        df_apoyos = self.get_dataframe_apoyos()
        df_ruedas = self.get_dataframe_ruedas()
        df_signos = self.get_dataframe_signos()
        
        combina = Combina2DF(self.pd)
        df = self.pd.DataFrame()
        try:
            df = combina.merge_dataframes(df_db, df_grupos)
            df = combina.merge_dataframes(df, df_relaciones)
            df = combina.merge_dataframes(df, df_apoyos)
            df = combina.merge_dataframes(df, df_ruedas)
            df = combina.merge_dataframes(df, df_signos)
        except Exception as e:
            print('Exception en CntImplantaciones.implantaciones_1:', e)
        
        return df
    