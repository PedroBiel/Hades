# -*- coding: utf-8 -*-
"""
Dialog with information of the version in QTextEdit

Created on 14.05.2020

__author__ = Pedro Biel
__version__ = 0.0.0
__email__ = pbiel@taimweser.com
"""


from PyQt5 import uic
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QDialog

from dlg_version.controller.cnt_version import CntVersion


class DlgVersion(QDialog):
    
    def __init__(self, parent=None):
        """Dialog with information of the version in QTextEdit."""
        
        QDialog.__init__(self, parent)
        uic.loadUi('dlg_version/view/dlg_version.ui', self)
        
        # Objects of the application.
        self.version = ''  # Versions of the application.
        
        # Instances of classes.
        self.cnt_version = CntVersion(self)
        
        # PyQt objects.
        self.txt_version = self.textEdit_version
        self.txt_version.setReadOnly(True)
        self.txt_version.setCurrentFont(QFont('Consolas', 10))
        self.btn_ok = self.pushButton_ok
        
        # Add items to QTextEdit.
        self.version = self.cnt_version.app_version()
        self.txt_version.setText(self.version)
        
        # Events.
        self.btn_ok.clicked.connect(self.close)
