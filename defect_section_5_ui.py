# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'defect_section_5_ui.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(250, 250)
        Form.setMinimumSize(QSize(250, 250))
        Form.setMaximumSize(QSize(250, 250))
        self.layoutWidget = QWidget(Form)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 10, 231, 234))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.layoutWidget)
        self.label_7.setObjectName(u"label_7")
        font = QFont()
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet(u"QLabel {\n"
"    border: 2px solid black;\n"
"    border-radius: 4px;\n"
"    padding: 2px;\n"
"}\n"
"")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_7)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_9 = QLabel(self.layoutWidget)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_2.addWidget(self.label_9, 2, 0, 1, 1)

        self.label_11 = QLabel(self.layoutWidget)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_2.addWidget(self.label_11, 3, 0, 1, 1)

        self.label_12 = QLabel(self.layoutWidget)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_2.addWidget(self.label_12, 1, 0, 1, 1)

        self.line_stretching_edit = QDoubleSpinBox(self.layoutWidget)
        self.line_stretching_edit.setObjectName(u"line_stretching_edit")
        self.line_stretching_edit.setMinimum(-10.000000000000000)
        self.line_stretching_edit.setMaximum(10.000000000000000)
        self.line_stretching_edit.setSingleStep(0.500000000000000)
        self.line_stretching_edit.setValue(1.000000000000000)

        self.gridLayout_2.addWidget(self.line_stretching_edit, 0, 1, 1, 1)

        self.line_shift_edit = QDoubleSpinBox(self.layoutWidget)
        self.line_shift_edit.setObjectName(u"line_shift_edit")
        self.line_shift_edit.setMinimum(-0.200000000000000)
        self.line_shift_edit.setMaximum(0.200000000000000)
        self.line_shift_edit.setSingleStep(0.010000000000000)
        self.line_shift_edit.setValue(0.000000000000000)

        self.gridLayout_2.addWidget(self.line_shift_edit, 1, 1, 1, 1)

        self.label_10 = QLabel(self.layoutWidget)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_2.addWidget(self.label_10, 0, 0, 1, 1)

        self.width_edit = QDoubleSpinBox(self.layoutWidget)
        self.width_edit.setObjectName(u"width_edit")
        self.width_edit.setMinimum(0.050000000000000)
        self.width_edit.setMaximum(0.200000000000000)
        self.width_edit.setSingleStep(0.010000000000000)
        self.width_edit.setValue(0.100000000000000)

        self.gridLayout_2.addWidget(self.width_edit, 3, 1, 1, 1)

        self.height_edit = QDoubleSpinBox(self.layoutWidget)
        self.height_edit.setObjectName(u"height_edit")
        self.height_edit.setMinimum(-10.000000000000000)
        self.height_edit.setMaximum(10.000000000000000)
        self.height_edit.setValue(-1.000000000000000)

        self.gridLayout_2.addWidget(self.height_edit, 2, 1, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout_2)

        self.createDefect_button = QPushButton(self.layoutWidget)
        self.createDefect_button.setObjectName(u"createDefect_button")

        self.verticalLayout_2.addWidget(self.createDefect_button)

        self.show_graph_button = QPushButton(self.layoutWidget)
        self.show_graph_button.setObjectName(u"show_graph_button")

        self.verticalLayout_2.addWidget(self.show_graph_button)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Line", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"Line", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"Height:", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"Width:", None))
#if QT_CONFIG(tooltip)
        self.label_12.setToolTip(QCoreApplication.translate("Form", u"Shift", None))
#endif // QT_CONFIG(tooltip)
        self.label_12.setText(QCoreApplication.translate("Form", u"b:", None))
#if QT_CONFIG(tooltip)
        self.label_10.setToolTip(QCoreApplication.translate("Form", u"Stretching", None))
#endif // QT_CONFIG(tooltip)
        self.label_10.setText(QCoreApplication.translate("Form", u"k:", None))
        self.createDefect_button.setText(QCoreApplication.translate("Form", u"Create Defect", None))
        self.show_graph_button.setText(QCoreApplication.translate("Form", u"Show 3D Surface", None))
    # retranslateUi

