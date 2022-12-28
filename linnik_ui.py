# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'linnik_ui.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(934, 651)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(934, 651))
        MainWindow.setMaximumSize(QSize(934, 651))
        self.actionSave_Parameters = QAction(MainWindow)
        self.actionSave_Parameters.setObjectName(u"actionSave_Parameters")
        self.actionAdd_Deffect = QAction(MainWindow)
        self.actionAdd_Deffect.setObjectName(u"actionAdd_Deffect")
        self.actionLoad_Parameters = QAction(MainWindow)
        self.actionLoad_Parameters.setObjectName(u"actionLoad_Parameters")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 600, 600))
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet(u"QLabel {\n"
"	 border: 2px solid black;\n"
"     border-radius: 4px;\n"
"     padding: 2px;\n"
"}")
        self.label.setScaledContents(True)
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(616, 20, 302, 150))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.alphaEdit = QDoubleSpinBox(self.layoutWidget)
        self.alphaEdit.setObjectName(u"alphaEdit")
        self.alphaEdit.setMinimum(0.010000000000000)
        self.alphaEdit.setMaximum(0.990000000000000)
        self.alphaEdit.setSingleStep(0.010000000000000)
        self.alphaEdit.setValue(0.200000000000000)

        self.gridLayout.addWidget(self.alphaEdit, 2, 1, 1, 1)

        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)

        self.wavelengthEdit = QSpinBox(self.layoutWidget)
        self.wavelengthEdit.setObjectName(u"wavelengthEdit")
        self.wavelengthEdit.setMaximum(1000)
        self.wavelengthEdit.setSingleStep(10)
        self.wavelengthEdit.setValue(540)

        self.gridLayout.addWidget(self.wavelengthEdit, 1, 1, 1, 1)

        self.yAngleEdit = QDoubleSpinBox(self.layoutWidget)
        self.yAngleEdit.setObjectName(u"yAngleEdit")
        self.yAngleEdit.setDecimals(4)
        self.yAngleEdit.setMaximum(360.000000000000000)

        self.gridLayout.addWidget(self.yAngleEdit, 0, 2, 1, 1)

        self.resolutionEdit = QSpinBox(self.layoutWidget)
        self.resolutionEdit.setObjectName(u"resolutionEdit")
        self.resolutionEdit.setMinimum(600)
        self.resolutionEdit.setMaximum(3000)
        self.resolutionEdit.setSingleStep(300)
        self.resolutionEdit.setValue(900)

        self.gridLayout.addWidget(self.resolutionEdit, 3, 1, 1, 1)

        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)

        self.xAngleEdit = QDoubleSpinBox(self.layoutWidget)
        self.xAngleEdit.setObjectName(u"xAngleEdit")
        self.xAngleEdit.setDecimals(4)
        self.xAngleEdit.setMaximum(1.000000000000000)
        self.xAngleEdit.setSingleStep(0.001000000000000)
        self.xAngleEdit.setValue(0.002000000000000)

        self.gridLayout.addWidget(self.xAngleEdit, 0, 1, 1, 1)

        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.label_6 = QLabel(self.layoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 4, 0, 1, 1)

        self.gMinEdit = QSpinBox(self.layoutWidget)
        self.gMinEdit.setObjectName(u"gMinEdit")
        self.gMinEdit.setMaximum(255)
        self.gMinEdit.setValue(100)

        self.gridLayout.addWidget(self.gMinEdit, 4, 1, 1, 1)

        self.gMaxEdit = QSpinBox(self.layoutWidget)
        self.gMaxEdit.setObjectName(u"gMaxEdit")
        self.gMaxEdit.setMaximum(255)
        self.gMaxEdit.setValue(240)

        self.gridLayout.addWidget(self.gMaxEdit, 4, 2, 1, 1)

        self.setParametersButton = QPushButton(self.centralwidget)
        self.setParametersButton.setObjectName(u"setParametersButton")
        self.setParametersButton.setGeometry(QRect(769, 175, 143, 28))
        self.createButton = QPushButton(self.centralwidget)
        self.createButton.setObjectName(u"createButton")
        self.createButton.setGeometry(QRect(620, 175, 143, 28))
        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(625, 245, 281, 25))
        self.progressBar.setValue(0)
        self.graphButton = QPushButton(self.centralwidget)
        self.graphButton.setObjectName(u"graphButton")
        self.graphButton.setGeometry(QRect(620, 210, 291, 28))
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(610, 510, 311, 31))
        font = QFont()
        font.setPointSize(10)
        font.setUnderline(True)
        self.label_7.setFont(font)
        self.label_7.setAlignment(Qt.AlignCenter)
        self.layoutWidget1 = QWidget(self.centralwidget)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(612, 540, 311, 65))
        self.gridLayout_2 = QGridLayout(self.layoutWidget1)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.section_1_button_ellipse = QPushButton(self.layoutWidget1)
        self.section_1_button_ellipse.setObjectName(u"section_1_button_ellipse")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.section_1_button_ellipse.sizePolicy().hasHeightForWidth())
        self.section_1_button_ellipse.setSizePolicy(sizePolicy1)

        self.gridLayout_2.addWidget(self.section_1_button_ellipse, 0, 0, 1, 1)

        self.section_2_button_giperbola = QPushButton(self.layoutWidget1)
        self.section_2_button_giperbola.setObjectName(u"section_2_button_giperbola")
        sizePolicy1.setHeightForWidth(self.section_2_button_giperbola.sizePolicy().hasHeightForWidth())
        self.section_2_button_giperbola.setSizePolicy(sizePolicy1)

        self.gridLayout_2.addWidget(self.section_2_button_giperbola, 0, 1, 1, 1)

        self.section_3_button_parabola = QPushButton(self.layoutWidget1)
        self.section_3_button_parabola.setObjectName(u"section_3_button_parabola")
        sizePolicy1.setHeightForWidth(self.section_3_button_parabola.sizePolicy().hasHeightForWidth())
        self.section_3_button_parabola.setSizePolicy(sizePolicy1)

        self.gridLayout_2.addWidget(self.section_3_button_parabola, 0, 2, 1, 1)

        self.section_4_button_paraboloid = QPushButton(self.layoutWidget1)
        self.section_4_button_paraboloid.setObjectName(u"section_4_button_paraboloid")
        sizePolicy1.setHeightForWidth(self.section_4_button_paraboloid.sizePolicy().hasHeightForWidth())
        self.section_4_button_paraboloid.setSizePolicy(sizePolicy1)

        self.gridLayout_2.addWidget(self.section_4_button_paraboloid, 1, 0, 1, 1)

        self.section_5_button_line = QPushButton(self.layoutWidget1)
        self.section_5_button_line.setObjectName(u"section_5_button_line")
        sizePolicy1.setHeightForWidth(self.section_5_button_line.sizePolicy().hasHeightForWidth())
        self.section_5_button_line.setSizePolicy(sizePolicy1)

        self.gridLayout_2.addWidget(self.section_5_button_line, 1, 1, 1, 1)

        self.section_6_button_math = QPushButton(self.layoutWidget1)
        self.section_6_button_math.setObjectName(u"section_6_button_math")
        sizePolicy1.setHeightForWidth(self.section_6_button_math.sizePolicy().hasHeightForWidth())
        self.section_6_button_math.setSizePolicy(sizePolicy1)

        self.gridLayout_2.addWidget(self.section_6_button_math, 1, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 934, 26))
        self.menuData = QMenu(self.menubar)
        self.menuData.setObjectName(u"menuData")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuData.menuAction())
        self.menuData.addAction(self.actionAdd_Deffect)
        self.menuData.addAction(self.actionSave_Parameters)
        self.menuData.addAction(self.actionLoad_Parameters)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Linnik", None))
        self.actionSave_Parameters.setText(QCoreApplication.translate("MainWindow", u"Save Parameters ", None))
        self.actionAdd_Deffect.setText(QCoreApplication.translate("MainWindow", u"Select Defect", None))
        self.actionLoad_Parameters.setText(QCoreApplication.translate("MainWindow", u"Load Parameters", None))
        self.label.setText("")
#if QT_CONFIG(tooltip)
        self.label_5.setToolTip(QCoreApplication.translate("MainWindow", u"Image size (width = height)", None))
#endif // QT_CONFIG(tooltip)
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Image size (pix): ", None))
#if QT_CONFIG(tooltip)
        self.label_3.setToolTip(QCoreApplication.translate("MainWindow", u"Wavelength (nm)", None))
#endif // QT_CONFIG(tooltip)
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Wavelength (nm):", None))
#if QT_CONFIG(tooltip)
        self.label_4.setToolTip(QCoreApplication.translate("MainWindow", u"Percentage of light intensity that is reflected from the mirror", None))
#endif // QT_CONFIG(tooltip)
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Ir:", None))
#if QT_CONFIG(tooltip)
        self.label_2.setToolTip(QCoreApplication.translate("MainWindow", u"\u03b1 - angle of inclination of the mirror plane, \u03b2 - angle of rotation", None))
#endif // QT_CONFIG(tooltip)
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Angles (\u03b1, \u03b2) (deg): ", None))
#if QT_CONFIG(tooltip)
        self.label_6.setToolTip(QCoreApplication.translate("MainWindow", u"Intensity range (0..255), green channel", None))
#endif // QT_CONFIG(tooltip)
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"gMin, gMax:", None))
        self.setParametersButton.setText(QCoreApplication.translate("MainWindow", u"Effects Parameters", None))
        self.createButton.setText(QCoreApplication.translate("MainWindow", u"Create", None))
#if QT_CONFIG(tooltip)
        self.progressBar.setToolTip(QCoreApplication.translate("MainWindow", u"(\u3065\uff61\u25d5\u203f\u203f\u25d5\uff61)\u3065", None))
#endif // QT_CONFIG(tooltip)
        self.graphButton.setText(QCoreApplication.translate("MainWindow", u"Show 3D Surface", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Creating Defect:", None))
        self.section_1_button_ellipse.setText(QCoreApplication.translate("MainWindow", u"Ellipse", None))
        self.section_2_button_giperbola.setText(QCoreApplication.translate("MainWindow", u"Hyperbola", None))
        self.section_3_button_parabola.setText(QCoreApplication.translate("MainWindow", u"Pow", None))
        self.section_4_button_paraboloid.setText(QCoreApplication.translate("MainWindow", u"Paraboloid", None))
        self.section_5_button_line.setText(QCoreApplication.translate("MainWindow", u"Line", None))
        self.section_6_button_math.setText(QCoreApplication.translate("MainWindow", u"Math Functions", None))
        self.menuData.setTitle(QCoreApplication.translate("MainWindow", u"Menu", None))
    # retranslateUi

