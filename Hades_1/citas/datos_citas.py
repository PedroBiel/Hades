# -*- coding: utf-8 -*-
"""
DESCRIPCIÓN

Created on Wed Feb 24 14:13:40 2021

__author__ = Pedro Biel
__version__ = 0.0.0
__email__ = pbiel@taimweser.com
"""



class Quotes:
    """Randomly choose a quote from several csv files from GitHub."""
    
    def __init__(self, pd, random, l):
        """
        Initilize pandas, random and the values with the links to the GitHub 
        directory with the csv files.
        """
        
        self.pd = pd
        self.random = random
        self.url_citas = l[0]
        self.url_lider = l[1]
        self.url_quotes = l[2]
        self.url_zitate = l[3]
        
    def choose_quote(self):
        """
        Choose a quote from the csv files with quotes

        Returns
        -------
        quote : str
        """
        
        # Read quotes.
        data_citas = self.pd.read_table(self.url_citas, names=['Quotes'])
        data_lider = self.pd.read_table(self.url_lider, names=['Quotes'])
        data_quotes = self.pd.read_table(self.url_quotes, names=['Quotes'])
        data_zitate = self.pd.read_table(self.url_zitate, names=['Quotes'])
        
        # Concatenate DataFrames.
        data = self.pd.concat([
            data_citas, data_lider, data_quotes, data_zitate
            ])
        
        # To list.
        l = data['Quotes'].to_list()
        
        # Randomly choose.
        quote = self.random.choice(l)
        
        return quote

if __name__ == '__main__':
    
    import pandas as pd
    import random
    
    url_citas = 'https://raw.githubusercontent.com/PedroBiel/quotes/main/csv/citas.csv'
    url_lider = 'https://raw.githubusercontent.com/PedroBiel/quotes/main/csv/lider_ante_innovacion.csv'
    url_quotes = 'https://raw.githubusercontent.com/PedroBiel/quotes/main/csv/quotes.csv'
    url_zitate = 'https://raw.githubusercontent.com/PedroBiel/quotes/main/csv/zitate.csv'
    lst_citas = [url_citas, url_lider, url_quotes, url_zitate]
    
    quotes = Quotes(pd, random, lst_citas)
    print(quotes.choose_quote())
    
    