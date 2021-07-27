# -*- coding: utf-8 -*-
"""
HADES
Controller Version

Created on 14.05.2020

__author__ = Pedro Biel
__version__ = 0.0.0
__email__ = structural.eng.biel@gmail.com
"""


from dlg_version.data.version_data import VersionData


class CntVersion:
    
    def __init__(self, dialog):
        """Controller of the dialog Version."""
            
        self.d = dialog

    def app_version(self):
        
        versions = VersionData.VERSIONS
        
        return versions
        