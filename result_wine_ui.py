# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\table.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

# Autores: Sarmiento Bryan, Zhizhpon Eduardo

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QTableView
from PyQt5.QtCore import QAbstractTableModel, Qt
import pandas as pd
import numpy as np

import sys

class ResultWineUI(QtWidgets.QWidget):

    def __init__(self, parent = None, data = []):
        super(ResultWineUI, self).__init__()
        self.data_frame = data
        self.parent = parent
        self.model = pandasModel(data = self.data_frame)
        self.setupUi(self)

    def setupUi(self, ResultWidget):
        ResultWidget.setObjectName("ResultWidget")
        self.center()

        font = QtGui.QFont()
        font.setPointSize(10)
        
        ResultWidget.setFont(font)
        ResultWidget.setFocusPolicy(QtCore.Qt.NoFocus)
        self.gridLayout = QtWidgets.QGridLayout(ResultWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        
        self.label_1 = QtWidgets.QLabel("Resultados:")
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_1.setFont(font)
        self.label_1.setObjectName("label_1")

        self.gridLayout.addWidget(self.label_1, 0, 0, 1, 1)

        self.tableResultsView = QTableView()
        self.tableResultsView.setModel(self.model)
        self.tableResultsView.setWordWrap(True)
        self.tableResultsView.setAutoScroll(True)
        self.tableResultsView.setAutoScrollMargin(16)
        self.tableResultsView.setObjectName("tableResultsView")

        self.tableResultsView.horizontalHeader().setVisible(True)
        self.tableResultsView.horizontalHeader().setCascadingSectionResizes(True)
        self.tableResultsView.horizontalHeader().setDefaultSectionSize(140)
        self.tableResultsView.horizontalHeader().setHighlightSections(False)
        self.tableResultsView.horizontalHeader().setSortIndicatorShown(True)
        self.tableResultsView.horizontalHeader().setStretchLastSection(False)
        self.tableResultsView.verticalHeader().setVisible(False)

        self.retranslateUi(ResultWidget)
        QtCore.QMetaObject.connectSlotsByName(ResultWidget)

    def retranslateUi(self, ResultWidget):
        _translate = QtCore.QCoreApplication.translate

        ResultWidget.setWindowTitle(_translate("ResultWidget", "Resultados - Calidad de Vino"))

    def showResultsNewWine(self, text, similarity):
        self.label_1.setText(text)
        #distances = distances[0].reshape((len(distances[0]), 1))
        similarity = pd.DataFrame(data = similarity, columns = ['similarity'])
        #distances = pd.DataFrame(data = distances, columns = ['distances'])
        
        df_r = pd.concat([self.data_frame, similarity], axis = 1)
        df_r = df_r.sort_values(by=['similarity'], ascending=False)

        self.model = pandasModel(data = df_r)
        self.tableResultsView.setModel(None)
        self.tableResultsView.setModel(self.model)
        self.gridLayout.addWidget(self.tableResultsView, 1, 0, 1, 1)
        self.resize(1250, 525)
        self.center()
        self.show()

    def showTrainResults(self, text, data, data_names):
        
        self.label_1.setText(text)
        data_frames = []
        for i in range(len(data)):
            data_ = data[i].reshape((len(data[i]), 1))
            df = pd.DataFrame(data=data_, columns=[data_names[i]])
            data_frames.extend([df])
        df_r = pd.concat(data_frames, axis = 1)
        
        self.model = pandasModel(data = df_r)
        self.tableResultsView.setModel(None)
        self.tableResultsView.setModel(self.model)
        self.gridLayout.addWidget(self.tableResultsView, 1, 0, 1, 1)
        self.resize(750, 525)
        self.center()
        self.show()


    def center(self):
        qr = self.frameGeometry()
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        # from win32api import GetSystemMetrics
        # print("cp:\n", cp, "\nqr:\n", qr)

class pandasModel(QAbstractTableModel):

    def __init__(self, data):
        QAbstractTableModel.__init__(self)
        self._data = data

    def rowCount(self, parent=None):
        return self._data.shape[0]

    def columnCount(self, parnet=None):
        return self._data.shape[1]

    def data(self, index, role=Qt.DisplayRole):
        if index.isValid():
            if role == Qt.DisplayRole:
                return str(self._data.iloc[index.row(), index.column()])
        return None

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self._data.columns[col]
        return None

if __name__ == "__main__":
    ui = ResultWineUI()
    
