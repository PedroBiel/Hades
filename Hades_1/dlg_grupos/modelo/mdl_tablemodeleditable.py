# -*- coding: utf-8 -*-
"""
TableModel desde pandas

Created on Fri Nov 29 09:29:13 2019

__author__ = Pedro Biel
__version__ = 0.0.0
__email__ = pbiel@taimweser.com
"""


from PyQt5 import QtGui
from PyQt5.QtCore import QAbstractTableModel, Qt


class PandasModelEditable(QAbstractTableModel):

    def __init__(self, data):
        QAbstractTableModel.__init__(self)
        self._data = data

    def rowCount(self, parent=None):
        try:
            return self._data.shape[0]
        except AttributeError as e:
            print(e)

    def columnCount(self, parnet=None):
        try:
            return self._data.shape[1]
        except AttributeError as e:
            print(e)

    def data(self, index, role=Qt.DisplayRole):
        if index.isValid():

            if role == Qt.DisplayRole:

                return str(self._data.iloc[index.row(), index.column()])

            column_count = self.columnCount()
            
            for column in range(0, column_count):
                
                if (index.column() == column and role == Qt.TextAlignmentRole):

                    return Qt.AlignHCenter | Qt.AlignVCenter
                
            # Color de las columnas.
            if role == Qt.BackgroundRole and index.column() in (0, 1):
                return QtGui.QColor('#32414B')

        return None

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self._data.columns[col]
        
        return None

#https://stackoverflow.com/questions/41192293/make-qtableview-editable-when-model-is-pandas-dataframe

    def setData(self, index, value, role):
        if not index.isValid():
            return False
        
        if role != Qt.EditRole:
            return False
        
        row = index.row()
        
        if row < 0 or row >= len(self._data.values):
            return False
        
        column = index.column()
        if column < 0 or column >= self._data.columns.size:
            return False
        
        # self._data.iloc[row][column] = value
        self._data.iloc[row, column] = value
        self.dataChanged.emit(index, index)
        return True

    def flags(self, index):
        flags = super(self.__class__,self).flags(index)
        flags |= Qt.ItemIsEditable
        flags |= Qt.ItemIsSelectable
        flags |= Qt.ItemIsEnabled
        flags |= Qt.ItemIsDragEnabled
        flags |= Qt.ItemIsDropEnabled
        return flags
    



if __name__ == '__main__':
    
    import sys
    import pandas as pd
    from PyQt5.QtWidgets import QApplication, QTableView

    df = pd.DataFrame({'a': ['Mary', 'Jim', 'John'],
                        'b': [100, 200, 300],
                        'c': ['a', 'b', 'c']
                        })

    app = QApplication(sys.argv)
    model = PandasModelEditable(df)
    view = QTableView()
    view.setModel(model)
    view.resize(400, 200)
    view.show()
    sys.exit(app.exec_())
