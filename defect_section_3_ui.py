# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'defect_section_3_ui.ui'
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
        Form.resize(250, 280)
        Form.setMinimumSize(QSize(250, 280))
        Form.setMaximumSize(QSize(250, 280))
        self.layoutWidget = QWidget(Form)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 10, 231, 265))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setStyleSheet(u"QLabel {\n"
"    border: 2px solid black;\n"
"    border-radius: 4px;\n"
"    padding: 2px;\n"
"}\n"
"")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)

        self.label_6 = QLabel(self.layoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 3, 0, 1, 1)

        self.width_edit = QDoubleSpinBox(self.layoutWidget)
        self.width_edit.setObjectName(u"width_edit")
        self.width_edit.setMinimum(0.050000000000000)
        self.width_edit.setMaximum(0.200000000000000)
        self.width_edit.setSingleStep(0.010000000000000)
        self.width_edit.setValue(0.100000000000000)

        self.gridLayout.addWidget(self.width_edit, 4, 1, 1, 1)

        self.parabola_b_edit = QDoubleSpinBox(self.layoutWidget)
        self.parabola_b_edit.setObjectName(u"parabola_b_edit")
        self.parabola_b_edit.setMinimum(2.000000000000000)
        self.parabola_b_edit.setMaximum(6.000000000000000)
        self.parabola_b_edit.setSingleStep(0.500000000000000)
        self.parabola_b_edit.setValue(2.000000000000000)

        self.gridLayout.addWidget(self.parabola_b_edit, 1, 1, 1, 1)

        self.parabola_a_edit = QDoubleSpinBox(self.layoutWidget)
        self.parabola_a_edit.setObjectName(u"parabola_a_edit")
        self.parabola_a_edit.setMinimum(2.000000000000000)
        self.parabola_a_edit.setMaximum(6.000000000000000)
        self.parabola_a_edit.setSingleStep(0.500000000000000)
        self.parabola_a_edit.setValue(2.000000000000000)

        self.gridLayout.addWidget(self.parabola_a_edit, 0, 1, 1, 1)

        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1)

        self.label_7 = QLabel(self.layoutWidget)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 4, 0, 1, 1)

        self.height_edit = QDoubleSpinBox(self.layoutWidget)
        self.height_edit.setObjectName(u"height_edit")
        self.height_edit.setMinimum(-10.000000000000000)
        self.height_edit.setMaximum(10.000000000000000)
        self.height_edit.setValue(-1.000000000000000)

        self.gridLayout.addWidget(self.height_edit, 3, 1, 1, 1)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

        self.parabola_c_edit = QDoubleSpinBox(self.layoutWidget)
        self.parabola_c_edit.setObjectName(u"parabola_c_edit")
        self.parabola_c_edit.setMaximum(0.200000000000000)
        self.parabola_c_edit.setSingleStep(0.010000000000000)
        self.parabola_c_edit.setValue(0.100000000000000)

        self.gridLayout.addWidget(self.parabola_c_edit, 2, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.createDefect_button = QPushButton(self.layoutWidget)
        self.createDefect_button.setObjectName(u"createDefect_button")

        self.verticalLayout.addWidget(self.createDefect_button)

        self.show_graph_button = QPushButton(self.layoutWidget)
        self.show_graph_button.setObjectName(u"show_graph_button")

        self.verticalLayout.addWidget(self.show_graph_button)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Parabola", None))
        self.label.setText(QCoreApplication.translate("Form", u"Parabola", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"a:", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Height:", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"b:", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"Width:", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"c:", None))
        self.createDefect_button.setText(QCoreApplication.translate("Form", u"Create Defect", None))
        self.show_graph_button.setText(QCoreApplication.translate("Form", u"Show 3D Surface", None))
    # retranslateUi

