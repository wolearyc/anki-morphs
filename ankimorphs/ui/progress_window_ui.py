# Form implementation generated from reading ui file 'progress_window.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_ProgressWindow(object):
    def setupUi(self, ProgressWindow):
        ProgressWindow.setObjectName("ProgressWindow")
        ProgressWindow.resize(792, 506)
        self.centralwidget = QtWidgets.QWidget(parent=ProgressWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.calculateProgressPushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.calculateProgressPushButton.setMinimumSize(QtCore.QSize(0, 57))
        self.calculateProgressPushButton.setObjectName("calculateProgressPushButton")
        self.horizontalLayout_3.addWidget(self.calculateProgressPushButton, 0, QtCore.Qt.AlignmentFlag.AlignTop)
        self.horizontalLayout_2.addLayout(self.horizontalLayout_3)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(-1, 10, -1, 10)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.squareBracketsCheckBox = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.squareBracketsCheckBox.setObjectName("squareBracketsCheckBox")
        self.verticalLayout_10.addWidget(self.squareBracketsCheckBox)
        self.namesMorphemizerCheckBox = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.namesMorphemizerCheckBox.setObjectName("namesMorphemizerCheckBox")
        self.verticalLayout_10.addWidget(self.namesMorphemizerCheckBox)
        self.horizontalLayout_6.addLayout(self.verticalLayout_10)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.roundBracketsCheckBox = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.roundBracketsCheckBox.setObjectName("roundBracketsCheckBox")
        self.verticalLayout_9.addWidget(self.roundBracketsCheckBox)
        self.namesFileCheckBox = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.namesFileCheckBox.setObjectName("namesFileCheckBox")
        self.verticalLayout_9.addWidget(self.namesFileCheckBox)
        self.horizontalLayout_6.addLayout(self.verticalLayout_9)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.slimRoundBracketsCheckBox = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.slimRoundBracketsCheckBox.setObjectName("slimRoundBracketsCheckBox")
        self.verticalLayout_8.addWidget(self.slimRoundBracketsCheckBox)
        self.numbersCheckBox = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.numbersCheckBox.setObjectName("numbersCheckBox")
        self.verticalLayout_8.addWidget(self.numbersCheckBox)
        self.horizontalLayout_6.addLayout(self.verticalLayout_8)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.tablesTabWidget = QtWidgets.QTabWidget(parent=self.centralwidget)
        self.tablesTabWidget.setObjectName("tablesTabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.numericalTableWidget = QtWidgets.QTableWidget(parent=self.tab)
        self.numericalTableWidget.setObjectName("numericalTableWidget")
        self.numericalTableWidget.setColumnCount(6)
        self.numericalTableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.numericalTableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.numericalTableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.numericalTableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.numericalTableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.numericalTableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.numericalTableWidget.setHorizontalHeaderItem(5, item)
        self.verticalLayout_6.addWidget(self.numericalTableWidget)
        self.tablesTabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.percentTableWidget = QtWidgets.QTableWidget(parent=self.tab_2)
        self.percentTableWidget.setObjectName("percentTableWidget")
        self.percentTableWidget.setColumnCount(6)
        self.percentTableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.percentTableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.percentTableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.percentTableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.percentTableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.percentTableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.percentTableWidget.setHorizontalHeaderItem(5, item)
        self.verticalLayout_7.addWidget(self.percentTableWidget)
        self.tablesTabWidget.addTab(self.tab_2, "")
        self.verticalLayout_4.addWidget(self.tablesTabWidget)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)
        ProgressWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(ProgressWindow)
        self.tablesTabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(ProgressWindow)

    def retranslateUi(self, ProgressWindow):
        _translate = QtCore.QCoreApplication.translate
        ProgressWindow.setWindowTitle(_translate("ProgressWindow", "Progress Report"))
        self.calculateProgressPushButton.setText(_translate("ProgressWindow", "Calculate Progress Report"))
        self.label_3.setText(_translate("ProgressWindow", "Options (nonfunctional for now)"))
        self.squareBracketsCheckBox.setText(_translate("ProgressWindow", "Ignore content in square brackets []"))
        self.namesMorphemizerCheckBox.setText(_translate("ProgressWindow", "Ignore names found by morphemizer"))
        self.roundBracketsCheckBox.setText(_translate("ProgressWindow", "ignore content in round brackets（）"))
        self.namesFileCheckBox.setText(_translate("ProgressWindow", "Ignore names found in names.txt"))
        self.slimRoundBracketsCheckBox.setText(_translate("ProgressWindow", "ignore content in slim round brackets ()"))
        self.numbersCheckBox.setText(_translate("ProgressWindow", "Ignore numbers"))
        item = self.numericalTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("ProgressWindow", "Priority Range"))
        item = self.numericalTableWidget.horizontalHeaderItem(1)
        item.setText(_translate("ProgressWindow", "Unique Morphs"))
        item = self.numericalTableWidget.horizontalHeaderItem(2)
        item.setText(_translate("ProgressWindow", "Total Known"))
        item = self.numericalTableWidget.horizontalHeaderItem(3)
        item.setText(_translate("ProgressWindow", "Total Learning"))
        item = self.numericalTableWidget.horizontalHeaderItem(4)
        item.setText(_translate("ProgressWindow", "Total Unknown"))
        item = self.numericalTableWidget.horizontalHeaderItem(5)
        item.setText(_translate("ProgressWindow", "Total Missing"))
        self.tablesTabWidget.setTabText(self.tablesTabWidget.indexOf(self.tab), _translate("ProgressWindow", "Numerical"))
        item = self.percentTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("ProgressWindow", "Priority Range"))
        item = self.percentTableWidget.horizontalHeaderItem(1)
        item.setText(_translate("ProgressWindow", "Unique Morphs"))
        item = self.percentTableWidget.horizontalHeaderItem(2)
        item.setText(_translate("ProgressWindow", "% Known"))
        item = self.percentTableWidget.horizontalHeaderItem(3)
        item.setText(_translate("ProgressWindow", "% Learning"))
        item = self.percentTableWidget.horizontalHeaderItem(4)
        item.setText(_translate("ProgressWindow", "% Unknown"))
        item = self.percentTableWidget.horizontalHeaderItem(5)
        item.setText(_translate("ProgressWindow", "% Missing"))
        self.tablesTabWidget.setTabText(self.tablesTabWidget.indexOf(self.tab_2), _translate("ProgressWindow", "Percentage"))
