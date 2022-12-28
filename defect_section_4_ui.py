# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'defect_section_4_ui.ui'
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
        Form.resize(250, 300)
        Form.setMinimumSize(QSize(250, 300))
        Form.setMaximumSize(QSize(250, 300))
        self.layoutWidget = QWidget(Form)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 10, 231, 288))
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
        self.x_center_edit = QDoubleSpinBox(self.layoutWidget)
        self.x_center_edit.setObjectName(u"x_center_edit")
        self.x_center_edit.setMaximum(0.300000000000000)
        self.x_center_edit.setSingleStep(0.010000000000000)
        self.x_center_edit.setValue(0.100000000000000)

        self.gridLayout.addWidget(self.x_center_edit, 0, 1, 1, 1)

        self.height_edit = QDoubleSpinBox(self.layoutWidget)
        self.height_edit.setObjectName(u"height_edit")
        self.height_edit.setMinimum(-10.000000000000000)
        self.height_edit.setMaximum(10.000000000000000)
        self.height_edit.setValue(-1.000000000000000)

        self.gridLayout.addWidget(self.height_edit, 4, 1, 1, 1)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)

        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)

        self.paraboloid_a_edit = QDoubleSpinBox(self.layoutWidget)
        self.paraboloid_a_edit.setObjectName(u"paraboloid_a_edit")
        self.paraboloid_a_edit.setMinimum(0.050000000000000)
        self.paraboloid_a_edit.setMaximum(0.300000000000000)
        self.paraboloid_a_edit.setSingleStep(0.010000000000000)
        self.paraboloid_a_edit.setValue(0.050000000000000)

        self.gridLayout.addWidget(self.paraboloid_a_edit, 2, 1, 1, 1)

        self.paraboloid_b_edit = QDoubleSpinBox(self.layoutWidget)
        self.paraboloid_b_edit.setObjectName(u"paraboloid_b_edit")
        self.paraboloid_b_edit.setMinimum(0.050000000000000)
        self.paraboloid_b_edit.setMaximum(0.300000000000000)
        self.paraboloid_b_edit.setSingleStep(0.010000000000000)
        self.paraboloid_b_edit.setValue(0.050000000000000)

        self.gridLayout.addWidget(self.paraboloid_b_edit, 3, 1, 1, 1)

        self.y_center_edit = QDoubleSpinBox(self.layoutWidget)
        self.y_center_edit.setObjectName(u"y_center_edit")
        self.y_center_edit.setMaximum(0.300000000000000)
        self.y_center_edit.setSingleStep(0.010000000000000)
        self.y_center_edit.setValue(0.100000000000000)

        self.gridLayout.addWidget(self.y_center_edit, 1, 1, 1, 1)

        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)

        self.label_6 = QLabel(self.layoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 4, 0, 1, 1)


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
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Paraboloid", None))
        self.label.setText(QCoreApplication.translate("Form", u"Paraboloid", None))
#if QT_CONFIG(tooltip)
        self.label_2.setToolTip(QCoreApplication.translate("Form", u"Coordinates of the center of the surface", None))
#endif // QT_CONFIG(tooltip)
        self.label_2.setText(QCoreApplication.translate("Form", u"X_Center (mm):", None))
#if QT_CONFIG(tooltip)
        self.label_5.setToolTip(QCoreApplication.translate("Form", u"Half-axis on the axis OY", None))
#endif // QT_CONFIG(tooltip)
        self.label_5.setText(QCoreApplication.translate("Form", u"b (mm):", None))
#if QT_CONFIG(tooltip)
        self.label_4.setToolTip(QCoreApplication.translate("Form", u"Half-axis on the axis OX", None))
#endif // QT_CONFIG(tooltip)
        self.label_4.setText(QCoreApplication.translate("Form", u"a (mm):", None))
#if QT_CONFIG(tooltip)
        self.label_3.setToolTip(QCoreApplication.translate("Form", u"Coordinates of the center of the surface", None))
#endif // QT_CONFIG(tooltip)
        self.label_3.setText(QCoreApplication.translate("Form", u"Y_Center (mm):", None))
#if QT_CONFIG(tooltip)
        self.label_6.setToolTip(QCoreApplication.translate("Form", u"Defect height", None))
#endif // QT_CONFIG(tooltip)
        self.label_6.setText(QCoreApplication.translate("Form", u"Height (mcm):", None))
        self.createDefect_button.setText(QCoreApplication.translate("Form", u"Create Defect", None))
        self.show_graph_button.setText(QCoreApplication.translate("Form", u"Show 3D Surface", None))
    # retranslateUi

