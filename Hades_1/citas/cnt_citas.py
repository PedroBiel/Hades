# -*- coding: utf-8 -*-
"""
Controlador de citas

Created on Wed Feb 24 13:55:12 2021

__author__ = Pedro Biel
__version__ = 0.0.0
__email__ = pbiel@taimweser.com
"""


from citas.datos_citas import Quotes

class CntCitas:
    """
    Citas memorables.
    Selecciona una cita aleatoriamente de entre diferentes ficheros csv de
    GitHub.
    """
    
    def __init__(self, ventana):
        """
        Inicializa los valores con los links al directorio de GiyHub que 
        contiene los ficheros csv.
        
        url_citas  : str ; link a las citas en español.
        url_lider  : str ; link a las citas en español. 
        url_quotes : str ; link a las citas en inglés.
        url_zitate : str ; link a las citas en alemán.
        """
        
        self.v = ventana
        
        self.url_citas = 'https://raw.githubusercontent.com/PedroBiel/quotes/main/csv/citas.csv'
        self.url_lider = 'https://raw.githubusercontent.com/PedroBiel/quotes/main/csv/lider_ante_innovacion.csv'
        self.url_quotes = 'https://raw.githubusercontent.com/PedroBiel/quotes/main/csv/quotes.csv'
        self.url_zitate = 'https://raw.githubusercontent.com/PedroBiel/quotes/main/csv/zitate.csv'
        self.lst_citas = [
            self.url_citas, self.url_lider, self.url_quotes, self.url_zitate
            ]
        
    def get_pandas(self):
        """Getter de la librería pandas."""
        
        return self.v.pd
    
    def get_random(self):
        """Getter de la librería random."""
        
        return self.v.random
    
    def set_cita(self, quote):
        """Setter de la cita."""
        
        self.v.cita = quote
        
    def cita(self):
        """
        Selecciona una cita aleatoriamente.
        """
        
        pd = self.get_pandas()
        random = self.get_random()
        quotes = Quotes(pd, random, self.lst_citas)
        quote = quotes.choose_quote()
        
        self.set_cita(quote)
        