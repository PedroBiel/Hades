# -*- coding: utf-8 -*-
"""
Extrae los datos del QAbstractTableModel

Created on Fri Sep 25 10:48:59 2020

__author__ = Pedro Biel
__version__ = 0.0.0
__email__ = pbiel@taimweser.com
"""

import pandas as pd


class TableModelData:
    """Extrae los datos del QAbstratTableModel."""
    
    def __init__(self, model):
        """
        Sea model el modelo de QAbstractTableModel, extrae los datos y los
        convierte a un formato directamente legible por Python.
        
        https://stackoverflow.com/questions/21280061/get-data-from-every-cell-from-a-qtableview

        model : QAbstracTableModel
        
        """
        
        self.model = model
    
    def model_data(self):
        """
        Sea model el modelo de QAbstractTableModel, extrae los datos en una 
        lista anidada siendo las sublistas las columnas del modelo.

        Returns
        -------
        model_data : list
                     Lista anidada con las listas de las columnas del modelo.
        """
        model_data = []
        for col in range(self.model.columnCount()):
            model_data.append([])
            
            for row in range(self.model.rowCount()):
                index = self.model.index(row, col)
                model_data[col].append(self.model.data(index))

        return model_data
    
    def get_lista_model_data(self):
        """Getter de la lista de valores del modelo."""
        
        l_model_data = self.model_data()
        
        return l_model_data
    
    def get_d_model_data(self):
        """Getter del diccionario de valores del modelo."""
        
        d_model_data = {}
        keys = ['Apoyo', 'Ruedas']
        l_model_data = self.get_lista_model_data()
        for key, data in zip(keys, l_model_data):
            d_model_data[key] = data
            
        return d_model_data
    
    def get_df_model_data(self):
        """Getter del pandas DataFrame de valores del modelo."""
        
        d_model_data = self.get_d_model_data()
        df_model_data = pd.DataFrame(d_model_data)
        
        return df_model_data
        
            
        
    
    











if __name__ == '__main__':

    app = QApplication(sys.argv)

    qt_translator = QTranslator()
    qt_translator.load(
        'qtbase_' + QLocale.system().name(),
        QLibraryInfo.location(QLibraryInfo.TranslationsPath)
        )
    app.installTranslator(qt_translator)

    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())

    myapp = MainWindow()
    myapp.show()
    sys.exit(app.exec_())
