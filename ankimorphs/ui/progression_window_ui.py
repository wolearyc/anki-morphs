# Form implementation generated from reading ui file 'progression_window.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_ProgressionWindow(object):
    def setupUi(self, ProgressionWindow):
        ProgressionWindow.setObjectName("ProgressionWindow")
        ProgressionWindow.resize(748, 467)
        self.centralwidget = QtWidgets.QWidget(parent=ProgressionWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(-1, 0, -1, 10)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_6 = QtWidgets.QLabel(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_7.addWidget(self.label_6)
        self.morphPriorityCBox = QtWidgets.QComboBox(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.morphPriorityCBox.sizePolicy().hasHeightForWidth())
        self.morphPriorityCBox.setSizePolicy(sizePolicy)
        self.morphPriorityCBox.setSizeAdjustPolicy(QtWidgets.QComboBox.SizeAdjustPolicy.AdjustToContents)
        self.morphPriorityCBox.setPlaceholderText("")
        self.morphPriorityCBox.setObjectName("morphPriorityCBox")
        self.horizontalLayout_7.addWidget(self.morphPriorityCBox)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setToolTipDuration(4)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.cumulativeCheckBox = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.cumulativeCheckBox.setObjectName("cumulativeCheckBox")
        self.verticalLayout_10.addWidget(self.cumulativeCheckBox)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(False)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.lemmaRadioButton = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.lemmaRadioButton.setEnabled(True)
        self.lemmaRadioButton.setObjectName("lemmaRadioButton")
        self.horizontalLayout_2.addWidget(self.lemmaRadioButton)
        self.inflectionRadioButton = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.inflectionRadioButton.setEnabled(True)
        self.inflectionRadioButton.setObjectName("inflectionRadioButton")
        self.horizontalLayout_2.addWidget(self.inflectionRadioButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout_10.addLayout(self.horizontalLayout_2)
        self.horizontalLayout.addLayout(self.verticalLayout_10)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.minPrioritySpinBox = QtWidgets.QSpinBox(parent=self.centralwidget)
        self.minPrioritySpinBox.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.minPrioritySpinBox.setMinimum(1)
        self.minPrioritySpinBox.setMaximum(100000)
        self.minPrioritySpinBox.setSingleStep(500)
        self.minPrioritySpinBox.setObjectName("minPrioritySpinBox")
        self.horizontalLayout_3.addWidget(self.minPrioritySpinBox)
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.maxPrioritySpinBox = QtWidgets.QSpinBox(parent=self.centralwidget)
        self.maxPrioritySpinBox.setMinimum(1)
        self.maxPrioritySpinBox.setMaximum(50000)
        self.maxPrioritySpinBox.setSingleStep(500)
        self.maxPrioritySpinBox.setProperty("value", 10000)
        self.maxPrioritySpinBox.setObjectName("maxPrioritySpinBox")
        self.horizontalLayout_3.addWidget(self.maxPrioritySpinBox)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout_9.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.binSizeSpinBox = QtWidgets.QSpinBox(parent=self.centralwidget)
        self.binSizeSpinBox.setMinimum(100)
        self.binSizeSpinBox.setMaximum(10000)
        self.binSizeSpinBox.setSingleStep(100)
        self.binSizeSpinBox.setProperty("value", 500)
        self.binSizeSpinBox.setObjectName("binSizeSpinBox")
        self.horizontalLayout_4.addWidget(self.binSizeSpinBox)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.verticalLayout_9.addLayout(self.horizontalLayout_4)
        self.horizontalLayout.addLayout(self.verticalLayout_9)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_6.addLayout(self.verticalLayout)
        self.calculateProgressPushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.calculateProgressPushButton.sizePolicy().hasHeightForWidth())
        self.calculateProgressPushButton.setSizePolicy(sizePolicy)
        self.calculateProgressPushButton.setMinimumSize(QtCore.QSize(0, 57))
        self.calculateProgressPushButton.setObjectName("calculateProgressPushButton")
        self.horizontalLayout_6.addWidget(self.calculateProgressPushButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem3)
        self.exportMorphListPushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.exportMorphListPushButton.setObjectName("exportMorphListPushButton")
        self.horizontalLayout_5.addWidget(self.exportMorphListPushButton)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem4)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.qTabWidget = QtWidgets.QTabWidget(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.qTabWidget.sizePolicy().hasHeightForWidth())
        self.qTabWidget.setSizePolicy(sizePolicy)
        self.qTabWidget.setObjectName("qTabWidget")
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
        self.numericalTableWidget.horizontalHeader().setStretchLastSection(False)
        self.numericalTableWidget.verticalHeader().setVisible(False)
        self.numericalTableWidget.verticalHeader().setStretchLastSection(False)
        self.verticalLayout_6.addWidget(self.numericalTableWidget)
        self.qTabWidget.addTab(self.tab, "")
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
        self.percentTableWidget.verticalHeader().setVisible(False)
        self.verticalLayout_7.addWidget(self.percentTableWidget)
        self.qTabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.morphTableWidget = QtWidgets.QTableWidget(parent=self.tab_3)
        self.morphTableWidget.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.morphTableWidget.sizePolicy().hasHeightForWidth())
        self.morphTableWidget.setSizePolicy(sizePolicy)
        self.morphTableWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.morphTableWidget.setAutoFillBackground(False)
        self.morphTableWidget.setObjectName("morphTableWidget")
        self.morphTableWidget.setColumnCount(4)
        self.morphTableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.morphTableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.morphTableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.morphTableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.morphTableWidget.setHorizontalHeaderItem(3, item)
        self.morphTableWidget.verticalHeader().setVisible(False)
        self.verticalLayout_2.addWidget(self.morphTableWidget)
        self.qTabWidget.addTab(self.tab_3, "")
        self.verticalLayout_4.addWidget(self.qTabWidget)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)
        ProgressionWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(ProgressionWindow)
        self.morphPriorityCBox.setCurrentIndex(-1)
        self.qTabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(ProgressionWindow)

    def retranslateUi(self, ProgressionWindow):
        _translate = QtCore.QCoreApplication.translate
        ProgressionWindow.setWindowTitle(_translate("ProgressionWindow", "Progression"))
        self.label_6.setText(_translate("ProgressionWindow", "Morph Priority"))
        self.label_3.setText(_translate("ProgressionWindow", "Options"))
        self.cumulativeCheckBox.setText(_translate("ProgressionWindow", "Report cumulative statistics"))
        self.label.setToolTip(_translate("ProgressionWindow", "Changeable in settings"))
        self.label.setText(_translate("ProgressionWindow", "Morph evaluation mode:"))
        self.lemmaRadioButton.setToolTip(_translate("ProgressionWindow", "Changeable in settings"))
        self.lemmaRadioButton.setText(_translate("ProgressionWindow", "Lemma"))
        self.inflectionRadioButton.setToolTip(_translate("ProgressionWindow", "Changeable in settings"))
        self.inflectionRadioButton.setText(_translate("ProgressionWindow", "Inflection"))
        self.label_2.setText(_translate("ProgressionWindow", "Priority range:"))
        self.label_4.setText(_translate("ProgressionWindow", "to"))
        self.label_5.setText(_translate("ProgressionWindow", "Bin size:"))
        self.calculateProgressPushButton.setText(_translate("ProgressionWindow", "Calculate\n"
"Progress \n"
"Report"))
        self.exportMorphListPushButton.setText(_translate("ProgressionWindow", "Export Morph List"))
        item = self.numericalTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("ProgressionWindow", "Priority Range"))
        item = self.numericalTableWidget.horizontalHeaderItem(1)
        item.setText(_translate("ProgressionWindow", "Unique Morphs"))
        item = self.numericalTableWidget.horizontalHeaderItem(2)
        item.setText(_translate("ProgressionWindow", "Total Known"))
        item = self.numericalTableWidget.horizontalHeaderItem(3)
        item.setText(_translate("ProgressionWindow", "Total Learning"))
        item = self.numericalTableWidget.horizontalHeaderItem(4)
        item.setText(_translate("ProgressionWindow", "Total Unknown"))
        item = self.numericalTableWidget.horizontalHeaderItem(5)
        item.setText(_translate("ProgressionWindow", "Total Missing"))
        self.qTabWidget.setTabText(self.qTabWidget.indexOf(self.tab), _translate("ProgressionWindow", "Numerical"))
        item = self.percentTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("ProgressionWindow", "Priority Range"))
        item = self.percentTableWidget.horizontalHeaderItem(1)
        item.setText(_translate("ProgressionWindow", "Unique Morphs"))
        item = self.percentTableWidget.horizontalHeaderItem(2)
        item.setText(_translate("ProgressionWindow", "% Known"))
        item = self.percentTableWidget.horizontalHeaderItem(3)
        item.setText(_translate("ProgressionWindow", "% Learning"))
        item = self.percentTableWidget.horizontalHeaderItem(4)
        item.setText(_translate("ProgressionWindow", "% Unknown"))
        item = self.percentTableWidget.horizontalHeaderItem(5)
        item.setText(_translate("ProgressionWindow", "% Missing"))
        self.qTabWidget.setTabText(self.qTabWidget.indexOf(self.tab_2), _translate("ProgressionWindow", "Percentage"))
        item = self.morphTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("ProgressionWindow", "Priority"))
        item = self.morphTableWidget.horizontalHeaderItem(1)
        item.setText(_translate("ProgressionWindow", "Lemma"))
        item = self.morphTableWidget.horizontalHeaderItem(2)
        item.setText(_translate("ProgressionWindow", "Inflection"))
        item = self.morphTableWidget.horizontalHeaderItem(3)
        item.setText(_translate("ProgressionWindow", "Status"))
        self.qTabWidget.setTabText(self.qTabWidget.indexOf(self.tab_3), _translate("ProgressionWindow", "Morph List"))
