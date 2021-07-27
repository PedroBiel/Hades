# -*- coding: utf-8 -*-
"""
Controlador de la exportación de datos a Excel

Created on Wed Feb 17 13:29:02 2021

__author__ = Pedro Biel
__version__ = 0.0.1
__email__ = pbiel@taimweser.com

Versión 0.0.1: Se incluye una excepción en el pandas Excel writer.
"""


from pyqt5_clases.qfiledialog import FileDialog

from dlg_fichero.constantes_dlgfichero import Constantes


class CntExcel:
    """Controlador de la exportación de datos a Excel."""
    
    def __init__(self, ventana):
        """Crea la ventana de MainWindow."""
        
        self.v = ventana
        
        self.t0 = ''
        self.t1 = ''
        
    def get_pandas(self):
        """Getter de la librería pandas."""
        
        return self.v.pd
    
    def get_xlsxwriter(self):
        """Getter de la librería xlsxwriter."""
        
        return self.v.xlsxwriter
    
    def get_date(self):
        """Getter de la fecha."""
        
        return self.v.date
    
    def get_dataframe_grupos(self):
        """Getter del DataFrame Grupos."""
        
        return self.v.df_grupos.copy()
    
    def get_dataframe_relaciones(self):
        """Getter del DataFrame Relaciones."""
        
        return self.v.df_relaciones.copy()
    
    def get_dataframe_apoyos(self):
        """Getter del DataFrame Apoyos."""
        
        return self.v.df_apoyos.copy()
    
    def get_dataframe_ruedas(self):
        """Getter del DataFrame Ruedas."""
        
        return self.v.df_ruedas.copy()
    
    def get_dataframe_signos(self):
        """Getter del DataFrame Signos."""
        
        return self.v.df_signos.copy()
    
    def get_dataframe_implantaciones(self):
        """Getter del dataframe de implantaciones."""
        
        return self.v.df_implantaciones.copy()
    
    def get_dataframe_ap_gr(self):
        """
        Getter del dataframe de implantaciones agrupado por apoyo y grupo.
        """
        
        return self.v.df_impl_ap_gr.copy()
    
    def get_dataframe_ap_gr_modelo(self):
        """
        Getter del dataframe de implantaciones agrupado por apoyo y grupo y 
        haciendo referencia al modelo.
        """
        
        return self.v.df_impl_ap_gr_modelo.copy()
    
    def get_dataframe_gr_ap(self):
        """
        Getter del dataframe de implantaciones agrupado por grupo y apoyo.
        """
        
        return self.v.df_impl_gr_ap.copy()
    
    def get_dataframe_gr_ap_modelo(self):
        """
        Getter del dataframe de implantaciones agrupado por grupo y apoyo y 
        haciendo referencia al modelo.
        """
        
        return self.v.df_impl_gr_ap_modelo.copy()
    
    def get_ruta_nombre_xlsx(self):
        """Getter de la ruta y el nombre de la hoja Excel."""
        
        return self.v.ruta_nombre_xlsx
    
    def set_ruta_nombre_xlsx(self, ruta_nombre):
        """Setter de la ruta y el nombre de la hoja Excel."""
        
        self.v.ruta_nombre_xlsx = ruta_nombre
    
    def get_save_file_name(self):
        """
        Obtiene la ruta y el nombre del fichero a guardar de FileDialog.
        Type : str
        """
        
        constantes = Constantes()
        subtitulo = constantes.get_guardar_excel()
        tipo_fichero = constantes.get_tipo_ficheros_excel()
        pfad = FileDialog(subtitulo, '', tipo_fichero)
        self.set_ruta_nombre_xlsx(pfad.get_save_file_name())
        
    def get_proyecto(self):
        """Getter de los datos de proyecto."""
        
        return self.v.d_proyecto

    def crea_excel_implantaciones(self):
        """Transfiere los datos a la hoja Excel."""
        
        try:
            self.excel_implantaciones()
        except Exception as e:
            print('Exception:', e)
            self.v.message_box_xlsx()
          
    def excel_implantaciones(self):
        """Pandas Excel writer."""
        
        # Inicia cronómetro.
        #self.t0 = self.v.time.clock()
        self.t0 = self.v.time.perf_counter()
        
        pd = self.get_pandas()
        
        df_impl = self.get_dataframe_implantaciones()
        df_impl_ap_gr = self.get_dataframe_ap_gr()
        df_impl_ap_gr_modelo = self.get_dataframe_ap_gr_modelo()
        df_impl_gr_ap = self.get_dataframe_gr_ap()
        df_impl_gr_ap_modelo = self.get_dataframe_gr_ap_modelo()
        print('\ndf_impl')
        print(df_impl)  #TODO cuando se abre un proyecto existe este df.
        print('\ndf_impl_ap_gr')
        print(df_impl_ap_gr)
        print('\ndf_impl_ap_gr_modelo')
        print(df_impl_ap_gr_modelo)
        print('\ndf_impl_gr_ap')
        print(df_impl_gr_ap)
        print('\ndf_impl_gr_ap_modelo')
        print(df_impl_gr_ap_modelo)
        
        ruta_nombre_xlsx = self.get_ruta_nombre_xlsx()
        
        # Create a Pandas Excel writer using XlsxWriter as the engine.
        writer = pd.ExcelWriter(ruta_nombre_xlsx, engine='xlsxwriter')
        
        # Write Datos de proyecto
        ws = 'Datos de proyecto'
        
        ## Get the xlsxwriter workbook and worksheet objects.
        wb = writer.book
        ws = wb.add_worksheet(ws)
        ## Add some cell formats.
        format_proyecto = wb.add_format()
        format_proyecto.set_font_size(14)
        format_proyecto.set_bold()
        format_datos = wb.add_format()
        format_datos.set_font_size(12)
        ws.set_column('A:A', 15)
        ## Project data.
        d_proyecto = self.get_proyecto()
        date = self.get_date()
        today = date.today()
        ws.write('A1', today.strftime("%d/%m/%Y"))
        ws.write('A2', 'Proyecto:')
        ws.write('A3', 'Nombre:')
        ws.write('A4', 'Empresa:')
        ws.write('A5', 'Objeto:')
        ws.write('A6', 'Autor:')
        ws.write('A7', 'Comentario:')
        ws.write('B2', d_proyecto['proyecto'], format_proyecto)
        ws.write('B3', d_proyecto['nombre'], format_proyecto)
        ws.write('B4', d_proyecto['empresa'])
        ws.write('B5', d_proyecto['objeto'])
        ws.write('B6', d_proyecto['autor'])
        ws.write('B7', d_proyecto['comentario'])
        ## Hide screen and printed gridlines.
        ws.hide_gridlines(2)
        
        # Write df_impl
        ws = 'Tabla completa'
        df_impl.to_excel(writer, ws, startrow=1, header=False, index=False)
        
        ## Get the xlsxwriter workbook and worksheet objects.
        wb = writer.book
        ws = writer.sheets[ws]
        ## Add some cell formats.
        format1 = wb.add_format()
        format1.set_align('center')
        ws.set_column('A:A', 40)
        ws.set_column('B:I', 16, format1)
        ws.set_column('J:O', None, format1)
        ## Get the dimensions of the dataframe.
        (max_row, max_col) = df_impl.shape
        ## Create a list of column headers, to use in add_table().
        column_settings = [{'header': column} for column in df_impl.columns]
        ## Add the Excel table structure. Pandas will add the data.
        ws.add_table(0, 0, max_row, max_col - 1, {'columns': column_settings})
        ## Hide screen and printed gridlines.
        ws.hide_gridlines(2)
        
        # Write df_impl_ap_gr, df_impl_gr_ap
        ws = 'Tablas sin modelos'
        df_impl_ap_gr.to_excel(writer, ws)
        start_row = df_impl_ap_gr.shape[0] + 5
        df_impl_gr_ap.to_excel(writer, ws, startrow=start_row)
        
        ## Get the xlsxwriter workbook and worksheet objects.
        wb = writer.book
        ws = writer.sheets[ws]
        ## Add some cell formats.
        format2 = wb.add_format()
        format2.set_align('center')
        format3 = wb.add_format()
        format3.set_border(1)
        ws.set_column('A:B', 20)
        ws.set_column('C:N', None, format2)
        xlsxwriter = self.get_xlsxwriter()
        row_ini = 2
        col_ini = 2
        row_fin = row_ini + len(df_impl_ap_gr)
        col_fin = len(df_impl_ap_gr.columns) + 1
        ws.conditional_format(
            xlsxwriter.utility.xl_range(
                row_ini, col_ini, row_fin, col_fin), {
                    'type': 'no_errors', 'format': format3
                    }
                )
        row_ini = row_fin + 5
        col_ini = 2
        row_fin = row_ini + len(df_impl_gr_ap)
        col_fin = len(df_impl_gr_ap.columns) + 1
        ws.conditional_format(
            xlsxwriter.utility.xl_range(
                row_ini, col_ini, row_fin, col_fin), {
                    'type': 'no_errors', 'format': format3
                    }
                )
        ## Hide screen and printed gridlines.
        ws.hide_gridlines(2)
        
        # Write df_impl_ap_gr.T, df_impl_gr_ap.T
        ws = 'Tablas transpuestas sin modelos'
        df_impl_ap_gr.T.to_excel(writer, ws)
        start_col = df_impl_ap_gr.T.shape[1] + 3
        df_impl_gr_ap.T.to_excel(writer, ws, startcol=start_col)
        
        ## Get the xlsxwriter workbook and worksheet objects.
        wb = writer.book
        ws = writer.sheets[ws]
        ## Add some cell formats.
        ws.set_column('A:BZ', 20, format2)
        row_ini = 3
        col_ini = 2
        row_fin = row_ini + len(df_impl_ap_gr.T) - 1
        col_fin = len(df_impl_ap_gr.T.columns) + 1
        ws.conditional_format(
            xlsxwriter.utility.xl_range(
                row_ini, col_ini, row_fin, col_fin), {
                    'type': 'no_errors', 'format': format3
                    }
                )
        row_ini = row_ini
        col_ini = col_fin + 4
        row_fin = row_ini + len(df_impl_gr_ap.T) - 1
        col_fin = col_ini + len(df_impl_gr_ap.T.columns) - 1
        ws.conditional_format(
            xlsxwriter.utility.xl_range(
                row_ini, col_ini, row_fin, col_fin), {
                    'type': 'no_errors', 'format': format3
                    }
                )
        ## Hide screen and printed gridlines.
        ws.hide_gridlines(2)
        ## Freeze pane.
        ws.freeze_panes('C1')
        
        # Write df_impl_ap_gr, df_impl_gr_ap con modelos
        ws = 'Tablas con modelos'
        df_impl_ap_gr_modelo.to_excel(writer, ws)
        start_row = df_impl_ap_gr_modelo.shape[0] + 5
        df_impl_gr_ap_modelo.to_excel(writer, ws, startrow=start_row)
        
        ## Get the xlsxwriter workbook and worksheet objects.
        wb = writer.book
        ws = writer.sheets[ws]
        ## Add some cell formats.
        format2 = wb.add_format()
        format2.set_align('center')
        format3 = wb.add_format()
        format3.set_border(1)
        ws.set_column('A:B', 20)
        for c in range(ord('D'), ord('Z') + 1, 2):
            ws.set_column(chr(c) + ':' + chr(c), 20)
        ws.set_column('C:Z', None, format2)
        xlsxwriter = self.get_xlsxwriter()
        row_ini = 2
        col_ini = 2
        row_fin = row_ini + len(df_impl_ap_gr_modelo)
        col_fin = len(df_impl_ap_gr_modelo.columns) + 1
        ws.conditional_format(
            xlsxwriter.utility.xl_range(
                row_ini, col_ini, row_fin, col_fin), {
                    'type': 'no_errors', 'format': format3
                    }
                )
        row_ini = row_fin + 5
        col_ini = 2
        row_fin = row_ini + len(df_impl_gr_ap_modelo)
        col_fin = len(df_impl_gr_ap_modelo.columns) + 1
        ws.conditional_format(
            xlsxwriter.utility.xl_range(
                row_ini, col_ini, row_fin, col_fin), {
                    'type': 'no_errors', 'format': format3
                    }
                )
        ## Hide screen and printed gridlines.
        ws.hide_gridlines(2)
        
        # Write df_impl_ap_gr.T, df_impl_gr_ap.T con modelos
        ws = 'Tablas transpuestas con modelos'
        df_impl_ap_gr_modelo.T.to_excel(writer, ws)
        start_col = df_impl_ap_gr_modelo.T.shape[1] + 3
        df_impl_gr_ap_modelo.T.to_excel(writer, ws, startcol=start_col)
        
        ## Get the xlsxwriter workbook and worksheet objects.
        wb = writer.book
        ws = writer.sheets[ws]
        ## Add some cell formats.
        ws.set_column('A:BZ', 20, format2)
        row_ini = 3
        col_ini = 2
        row_fin = row_ini + len(df_impl_ap_gr_modelo.T) - 1
        col_fin = len(df_impl_ap_gr_modelo.T.columns) + 1
        ws.conditional_format(
            xlsxwriter.utility.xl_range(
                row_ini, col_ini, row_fin, col_fin), {
                    'type': 'no_errors', 'format': format3
                    }
                )
        row_ini = row_ini
        col_ini = col_fin + 4
        row_fin = row_ini + len(df_impl_gr_ap_modelo.T) - 1
        col_fin = col_ini + len(df_impl_gr_ap_modelo.T.columns) - 1
        ws.conditional_format(
            xlsxwriter.utility.xl_range(
                row_ini, col_ini, row_fin, col_fin), {
                    'type': 'no_errors', 'format': format3
                    }
                )
        ## Hide screen and printed gridlines.
        ws.hide_gridlines(2)
        ## Freeze pane.
        ws.freeze_panes('C1')

        # Close the Pandas Excel writer and output the Excel file.
        writer.save()
        
        # Cronometra.
        #self.t1 = self.v.time.clock()
        self.t1 = self.v.time.perf_counter()
        t = self.t1 - self.t0
        print('\nt', t)
        print('\nxlsx_tiempo', self.v.xlsx_tiempo)
        t = round((t + self.v.xlsx_tiempo), 2)  # Más el tiempo en crear los DataFrames de implantación.
        self.v.xlsx_tiempo = str(t) + ' s'
        
        # Salida PyQt5.
        self.v.salida_ruta_nombre_xlsx()
        
        # Status bar.
        text = 'Tablas Excel para los cuadros de implantación creadas con éxito.'
        self.v.status_bar(text)
