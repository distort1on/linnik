# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'defect_section_6_ui.ui'
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
        Form.resize(250, 340)
        Form.setMinimumSize(QSize(250, 340))
        Form.setMaximumSize(QSize(250, 340))
        self.layoutWidget = QWidget(Form)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 10, 231, 325))
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
        self.width_edit = QDoubleSpinBox(self.layoutWidget)
        self.width_edit.setObjectName(u"width_edit")
        self.width_edit.setDecimals(3)
        self.width_edit.setMinimum(0.002000000000000)
        self.width_edit.setMaximum(0.200000000000000)
        self.width_edit.setSingleStep(0.010000000000000)
        self.width_edit.setValue(0.070000000000000)

        self.gridLayout.addWidget(self.width_edit, 5, 1, 1, 1)

        self.math_X_Stretching_edit = QDoubleSpinBox(self.layoutWidget)
        self.math_X_Stretching_edit.setObjectName(u"math_X_Stretching_edit")
        self.math_X_Stretching_edit.setMinimum(5.000000000000000)
        self.math_X_Stretching_edit.setMaximum(20.000000000000000)
        self.math_X_Stretching_edit.setSingleStep(1.000000000000000)
        self.math_X_Stretching_edit.setValue(15.000000000000000)

        self.gridLayout.addWidget(self.math_X_Stretching_edit, 1, 1, 1, 1)

        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)

        self.label_6 = QLabel(self.layoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 4, 0, 1, 1)

        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.math_X_Shift_edit = QDoubleSpinBox(self.layoutWidget)
        self.math_X_Shift_edit.setObjectName(u"math_X_Shift_edit")
        self.math_X_Shift_edit.setMinimum(-0.200000000000000)
        self.math_X_Shift_edit.setMaximum(0.200000000000000)
        self.math_X_Shift_edit.setSingleStep(0.010000000000000)
        self.math_X_Shift_edit.setValue(0.000000000000000)

        self.gridLayout.addWidget(self.math_X_Shift_edit, 2, 1, 1, 1)

        self.math_Y_Shift_edit = QDoubleSpinBox(self.layoutWidget)
        self.math_Y_Shift_edit.setObjectName(u"math_Y_Shift_edit")
        self.math_Y_Shift_edit.setMinimum(-0.200000000000000)
        self.math_Y_Shift_edit.setMaximum(0.200000000000000)
        self.math_Y_Shift_edit.setSingleStep(0.010000000000000)
        self.math_Y_Shift_edit.setValue(0.000000000000000)

        self.gridLayout.addWidget(self.math_Y_Shift_edit, 3, 1, 1, 1)

        self.label_13 = QLabel(self.layoutWidget)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout.addWidget(self.label_13, 5, 0, 1, 1)

        self.height_edit = QDoubleSpinBox(self.layoutWidget)
        self.height_edit.setObjectName(u"height_edit")
        self.height_edit.setMinimum(-10.000000000000000)
        self.height_edit.setMaximum(10.000000000000000)
        self.height_edit.setValue(-3.000000000000000)

        self.gridLayout.addWidget(self.height_edit, 4, 1, 1, 1)

        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)

        self.math_Y_Stretching_edit = QDoubleSpinBox(self.layoutWidget)
        self.math_Y_Stretching_edit.setObjectName(u"math_Y_Stretching_edit")
        self.math_Y_Stretching_edit.setMinimum(0.050000000000000)
        self.math_Y_Stretching_edit.setMaximum(0.400000000000000)
        self.math_Y_Stretching_edit.setSingleStep(0.010000000000000)
        self.math_Y_Stretching_edit.setValue(0.200000000000000)

        self.gridLayout.addWidget(self.math_Y_Stretching_edit, 0, 1, 1, 1)

        self.label_14 = QLabel(self.layoutWidget)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout.addWidget(self.label_14, 6, 0, 1, 1)

        self.math_graphic_type_edit = QComboBox(self.layoutWidget)
        self.math_graphic_type_edit.addItem("")
        self.math_graphic_type_edit.addItem("")
        self.math_graphic_type_edit.addItem("")
        self.math_graphic_type_edit.setObjectName(u"math_graphic_type_edit")

        self.gridLayout.addWidget(self.math_graphic_type_edit, 6, 1, 1, 1)


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
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Math Functions", None))
        self.label.setText(QCoreApplication.translate("Form", u"Math Functions", None))
#if QT_CONFIG(tooltip)
        self.label_4.setToolTip(QCoreApplication.translate("Form", u"Shift along the OX axis", None))
#endif // QT_CONFIG(tooltip)
        self.label_4.setText(QCoreApplication.translate("Form", u"c (mm):", None))
#if QT_CONFIG(tooltip)
        self.label_6.setToolTip(QCoreApplication.translate("Form", u"Defect height", None))
#endif // QT_CONFIG(tooltip)
        self.label_6.setText(QCoreApplication.translate("Form", u"Height (mcm):", None))
#if QT_CONFIG(tooltip)
        self.label_5.setToolTip(QCoreApplication.translate("Form", u"Shift along the OY axis", None))
#endif // QT_CONFIG(tooltip)
        self.label_5.setText(QCoreApplication.translate("Form", u"d (mm):", None))
#if QT_CONFIG(tooltip)
        self.label_2.setToolTip(QCoreApplication.translate("Form", u"Stretching / compression along the OY axis", None))
#endif // QT_CONFIG(tooltip)
        self.label_2.setText(QCoreApplication.translate("Form", u"a:", None))
#if QT_CONFIG(tooltip)
        self.label_13.setToolTip(QCoreApplication.translate("Form", u"Defect width", None))
#endif // QT_CONFIG(tooltip)
        self.label_13.setText(QCoreApplication.translate("Form", u"Width (mm):", None))
#if QT_CONFIG(tooltip)
        self.label_3.setToolTip(QCoreApplication.translate("Form", u"Stretching / compression along the OX axis", None))
#endif // QT_CONFIG(tooltip)
        self.label_3.setText(QCoreApplication.translate("Form", u"b:", None))
#if QT_CONFIG(tooltip)
        self.label_14.setToolTip(QCoreApplication.translate("Form", u"Defect type", None))
#endif // QT_CONFIG(tooltip)
        self.label_14.setText(QCoreApplication.translate("Form", u"Type:", None))
        self.math_graphic_type_edit.setItemText(0, QCoreApplication.translate("Form", u"sin", None))
        self.math_graphic_type_edit.setItemText(1, QCoreApplication.translate("Form", u"exp", None))
        self.math_graphic_type_edit.setItemText(2, QCoreApplication.translate("Form", u"tan", None))

        self.createDefect_button.setText(QCoreApplication.translate("Form", u"Create Defect", None))
        self.show_graph_button.setText(QCoreApplication.translate("Form", u"Show 3D Surface", None))
    # retranslateUi

