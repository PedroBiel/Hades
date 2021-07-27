# -*- coding: utf-8 -*-
"""
Dialog QWebEngineView

Created on 12.05.2020

__author__ = Pedro Biel
__version__ = 0.0.0
__email__ = pbiel@taimweser.com
"""


from PyQt5 import uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

from dlg_web.controller.cnt_web import CntWeb


class DlgWeb(QDialog):
    
    def __init__(self, parent=None):
        """Dialog QWebEngineView."""
        
        QDialog.__init__(self, parent)
        uic.loadUi('dlg_web/view/dlg_web.ui', self)
        self.resize(800, 600)
        
        # Objects of the application.
        self.url = ''  # URL adress.
        
        # Instances of classes.
        self.cnt_web = CntWeb(self)
        
        # PyQt objects.
        self.wev_url = self.webEngineView_url
        self.btn_ok = self.pushButton_ok
        
        # Add items to QLineEdit.
        self.url = self.cnt_web.url()
        self.wev_url.setUrl(QUrl(self.url))
        
        # Events.
        self.btn_ok.clicked.connect(self.close)
