# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'processingImageParameters_ui.ui'
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
        Form.resize(270, 420)
        Form.setMinimumSize(QSize(270, 420))
        Form.setMaximumSize(QSize(270, 420))
        Form.setStyleSheet(u"")
        self.layoutWidget = QWidget(Form)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(30, 10, 212, 400))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"QLabel {\n"
"    border: 2px solid black;\n"
"    border-radius: 4px;\n"
"    padding: 2px;\n"
"}")

        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.noise_sigmaEdit = QSpinBox(self.layoutWidget)
        self.noise_sigmaEdit.setObjectName(u"noise_sigmaEdit")
        self.noise_sigmaEdit.setMinimum(0)
        self.noise_sigmaEdit.setMaximum(50)
        self.noise_sigmaEdit.setValue(10)

        self.gridLayout.addWidget(self.noise_sigmaEdit, 0, 1, 1, 1)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.noise_muEdit = QSpinBox(self.layoutWidget)
        self.noise_muEdit.setObjectName(u"noise_muEdit")
        self.noise_muEdit.setMinimum(-20)
        self.noise_muEdit.setMaximum(20)

        self.gridLayout.addWidget(self.noise_muEdit, 1, 1, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_2)

        self.verticalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"QLabel {\n"
"    border: 2px solid black;\n"
"    border-radius: 4px;\n"
"    padding: 2px;\n"
"}")

        self.gridLayout_3.addWidget(self.label_4, 0, 0, 1, 1)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_4.addWidget(self.label_5, 1, 0, 1, 1)

        self.blur_radiusEdit = QSpinBox(self.layoutWidget)
        self.blur_radiusEdit.setObjectName(u"blur_radiusEdit")
        self.blur_radiusEdit.setMaximum(150)
        self.blur_radiusEdit.setSingleStep(5)
        self.blur_radiusEdit.setValue(80)

        self.gridLayout_4.addWidget(self.blur_radiusEdit, 1, 1, 1, 1)

        self.label_6 = QLabel(self.layoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_4.addWidget(self.label_6, 0, 0, 1, 1)

        self.blur_sigmaEdit = QSpinBox(self.layoutWidget)
        self.blur_sigmaEdit.setObjectName(u"blur_sigmaEdit")
        self.blur_sigmaEdit.setMaximum(20)
        self.blur_sigmaEdit.setSingleStep(1)
        self.blur_sigmaEdit.setValue(10)

        self.gridLayout_4.addWidget(self.blur_sigmaEdit, 0, 1, 1, 1)

        self.label_11 = QLabel(self.layoutWidget)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_4.addWidget(self.label_11, 2, 0, 1, 1)

        self.blur_coreEdit = QSpinBox(self.layoutWidget)
        self.blur_coreEdit.setObjectName(u"blur_coreEdit")
        self.blur_coreEdit.setReadOnly(False)
        self.blur_coreEdit.setMinimum(3)
        self.blur_coreEdit.setMaximum(9)
        self.blur_coreEdit.setSingleStep(2)
        self.blur_coreEdit.setValue(5)

        self.gridLayout_4.addWidget(self.blur_coreEdit, 2, 1, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_4, 1, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_3)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.vignette_saturationEdit = QDoubleSpinBox(self.layoutWidget)
        self.vignette_saturationEdit.setObjectName(u"vignette_saturationEdit")
        self.vignette_saturationEdit.setDecimals(2)
        self.vignette_saturationEdit.setMinimum(0.500000000000000)
        self.vignette_saturationEdit.setMaximum(2.000000000000000)
        self.vignette_saturationEdit.setSingleStep(0.100000000000000)
        self.vignette_saturationEdit.setValue(1.400000000000000)

        self.gridLayout_5.addWidget(self.vignette_saturationEdit, 2, 1, 1, 1)

        self.vignette_alphaEdit = QDoubleSpinBox(self.layoutWidget)
        self.vignette_alphaEdit.setObjectName(u"vignette_alphaEdit")
        self.vignette_alphaEdit.setMaximum(2.000000000000000)
        self.vignette_alphaEdit.setValue(1.000000000000000)

        self.gridLayout_5.addWidget(self.vignette_alphaEdit, 1, 1, 1, 1)

        self.label_10 = QLabel(self.layoutWidget)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_5.addWidget(self.label_10, 2, 0, 1, 1)

        self.label_7 = QLabel(self.layoutWidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"QLabel {\n"
"    border: 2px solid black;\n"
"    border-radius: 4px;\n"
"    padding: 2px;\n"
"}")

        self.gridLayout_5.addWidget(self.label_7, 0, 0, 1, 2)

        self.label_8 = QLabel(self.layoutWidget)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_5.addWidget(self.label_8, 1, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_5)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Parameters", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"NOISE", None))
#if QT_CONFIG(tooltip)
        self.label_2.setToolTip(QCoreApplication.translate("Form", u"Mean", None))
#endif // QT_CONFIG(tooltip)
        self.label_2.setText(QCoreApplication.translate("Form", u"Mu:", None))
#if QT_CONFIG(tooltip)
        self.label.setToolTip(QCoreApplication.translate("Form", u"Standard deviation (noise level)", None))
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("Form", u"Sigma:", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"BLUR", None))
#if QT_CONFIG(tooltip)
        self.label_5.setToolTip(QCoreApplication.translate("Form", u"Focus radius", None))
#endif // QT_CONFIG(tooltip)
        self.label_5.setText(QCoreApplication.translate("Form", u"Radius:", None))
#if QT_CONFIG(tooltip)
        self.label_6.setToolTip(QCoreApplication.translate("Form", u"Blur degree", None))
#endif // QT_CONFIG(tooltip)
        self.label_6.setText(QCoreApplication.translate("Form", u"Sigma:", None))
#if QT_CONFIG(tooltip)
        self.blur_sigmaEdit.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.label_11.setToolTip(QCoreApplication.translate("Form", u"Convolution kernel size (blur diameter of the area around the pixel)", None))
#endif // QT_CONFIG(tooltip)
        self.label_11.setText(QCoreApplication.translate("Form", u"Core_Width:", None))
#if QT_CONFIG(tooltip)
        self.label_10.setToolTip(QCoreApplication.translate("Form", u"Image saturation", None))
#endif // QT_CONFIG(tooltip)
        self.label_10.setText(QCoreApplication.translate("Form", u"Saturation:", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"VIGNETTE", None))
#if QT_CONFIG(tooltip)
        self.label_8.setToolTip(QCoreApplication.translate("Form", u"Overlap degree", None))
#endif // QT_CONFIG(tooltip)
        self.label_8.setText(QCoreApplication.translate("Form", u"Radius:", None))
    # retranslateUi

