# -*- coding: utf-8 -*-
"""
PyQt5 pills
MessageBox

Created on 04.05.2020

__author__ = Pedro Biel
__version__ = 0.0.0
__email__ = structural.eng.biel@gmail.com
"""


from PyQt5.QtWidgets import QMessageBox


class MessageBox:
    
    def __init__(self, window_title, text, info_text, detail_text=''):
        """
        Display informational messages.
        
        setStandardButtons():   
            QMessageBox.Ok
            QMessageBox.Open
            QMessageBox.Save
            QMessageBox.Cancel
            QMessageBox.Close
            QMessageBox.Yes
            QMessageBox.No
            QMessageBox.Abort
            QMessageBox.Retry
            QMessageBox.Ignore

        e.g.: msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        """
        self.window_title = window_title
        self.text = text
        self.info_text = info_text
        self.detail_text = detail_text
        
        self.msg = QMessageBox()
        
    def critical(self):
        """Provides a modal dialog for reporting critical errors."""

        self.msg.setIcon(QMessageBox.Critical)
        self.msg.setWindowTitle(self.window_title)
        self.msg.setText(self.text)
        self.msg.setInformativeText(self.info_text)
        self.msg.setStandardButtons(QMessageBox.Ok)
        self.msg.exec_()
    
    def information(self):
        """Provides a modal dialog reporting information about normal operations."""

        self.msg.setIcon(QMessageBox.Information)
        self.msg.setWindowTitle(self.window_title)
        self.msg.setText(self.text)
        self.msg.setInformativeText(self.info_text)
        self.msg.setStandardButtons(QMessageBox.Ok)
        self.msg.exec_()
    
    def question(self):
        """Provides a modal dialog asking a question during normal operations."""

        self.msg.setIcon(QMessageBox.Question)
        self.msg.setWindowTitle(self.window_title)
        self.msg.setText(self.text)
        self.msg.setInformativeText(self.info_text)
        self.msg.setStandardButtons(QMessageBox.Ok)
        self.msg.exec_()
    
    def warning(self):
        """Provides a modal dialog reporting non-critical errors."""

        self.msg.setIcon(QMessageBox.Warning)
        self.msg.setWindowTitle(self.window_title)
        self.msg.setText(self.text)
        self.msg.setInformativeText(self.info_text)
        self.msg.setStandardButtons(QMessageBox.Ok)
        self.msg.exec_()
    
    def critical_detailed_text(self):
        """Provides a modal dialog for reporting critical errors."""

        self.msg.setIcon(QMessageBox.Critical)
        self.msg.setWindowTitle(self.window_title)
        self.msg.setText(self.text)
        self.msg.setInformativeText(self.info_text)
        self.msg.setDetailedText(self.detail_text)
        self.msg.setStandardButtons(QMessageBox.Ok)
        self.msg.exec_()
    
    def information_detailed_text(self):
        """Provides a modal dialog reporting information about normal operations."""

        self.msg.setIcon(QMessageBox.Information)
        self.msg.setWindowTitle(self.window_title)
        self.msg.setText(self.text)
        self.msg.setInformativeText(self.info_text)
        self.msg.setDetailedText(self.detail_text)
        self.msg.setStandardButtons(QMessageBox.Ok)
        self.msg.exec_()
    
    def question_detailed_text(self):
        """Provides a modal dialog asking a question during normal operations."""

        self.msg.setIcon(QMessageBox.Question)
        self.msg.setWindowTitle(self.window_title)
        self.msg.setText(self.text)
        self.msg.setInformativeText(self.info_text)
        self.msg.setDetailedText(self.detail_text)
        self.msg.setStandardButtons(QMessageBox.Ok)
        self.msg.exec_()
    
    def warning_detailed_text(self):
        """Provides a modal dialog reporting non-critical errors."""

        self.msg.setIcon(QMessageBox.Warning)
        self.msg.setWindowTitle(self.window_title)
        self.msg.setText(self.text)
        self.msg.setInformativeText(self.info_text)
        self.msg.setDetailedText(self.detail_text)
        self.msg.setStandardButtons(QMessageBox.Ok)
        self.msg.exec_()
        