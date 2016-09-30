'''
Created on Mar 23, 2013

@author: Tree
'''
import sys
from PyQt4 import QtGui
from jvRater.main import MainWindow


application = QtGui.QApplication(sys.argv)
window = MainWindow()
window.show()
application.exec_()