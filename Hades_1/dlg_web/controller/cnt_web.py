# -*- coding: utf-8 -*-
"""
Controller QWebEngineView

Created on 12.05.2020

__author__ = Pedro Biel
__version__ = 1.0.0
__email__ = structural.eng.biel@gmail.com
"""


from dlg_web.data.initial_data import WebData


class CntWeb:
    
    def __init__(self, dialog):
        """Controller of the dialog QWebEngineView."""
        
        self.d = dialog


    def url(self):
        
        url_name = WebData.INITIAL_DATA
        
        return url_name
