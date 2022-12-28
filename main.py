#  Copyright (c) 2021 Illia Popov - All rights reserved.

from PIL import Image
import warnings
import os
from PySide2.QtCore import QSettings
import PySide2 as PS
from PySide2.QtCore import QObject, QThread, Signal, Slot
#os.popen("pyside2-uic linnik_ui.ui -o linnik_ui.py")
import math
import pylab
from mpl_toolkits.mplot3d import Axes3D
from scipy import interpolate
import numpy as np
import random
import cv2
from PySide2.QtWidgets import QSpinBox, QDoubleSpinBox
from PySide2 import QtWidgets, QtGui
from PySide2.QtWidgets import QFileDialog, QDesktopWidget
from linnik_ui import Ui_MainWindow
from processingImageParameters_ui import Ui_Form
from defect_section_1_ui import Ui_Form as section_1_Ui_Form
from defect_section_2_ui import Ui_Form as section_2_Ui_Form
from defect_section_3_ui import Ui_Form as section_3_Ui_Form
from defect_section_4_ui import Ui_Form as section_4_Ui_Form
from defect_section_5_ui import Ui_Form as section_5_Ui_Form
from defect_section_6_ui import Ui_Form as section_6_Ui_Form
import making_height_matix as MATRIX_CREATOR
import qtmodern.styles
import qtmodern.windows
import sys
from matplotlib import cm
import matplotlib
from artefacts import artef_list as ARTEFACTS_LIST

matplotlib.use("Qt5Agg")

X_SIZE = 0
Y_SIZE = 0

DEFECT_NAME = ""


class Worker(QObject):
    """
    Creating a worker object by subclassing QObject and put my long-running task in it.
    """
    def __init__(self, resultName):
        super().__init__()
        self.resultName = resultName

    finished = Signal()
    progress = Signal(int)

    def run(self):
        try:
            global X_SIZE, Y_SIZE
            X_SIZE = interface.resolutionEdit.value()
            Y_SIZE = X_SIZE
            print(X_SIZE, Y_SIZE)

            self.progress.emit(0)
            make_spline()
            self.progress.emit(30)

            image = create_image(X_SIZE, Y_SIZE)

            interf = make_interf(image)
        
           
            self.progress.emit(70)

            noise = make_noise(interf)
            

            self.progress.emit(80)

            blur1 = first_blur_image(noise)
           

            blur2 = radial_blur_image(blur1)
            

            self.progress.emit(90)

            result = make_vignette(blur2)
            

            self.progress.emit(100)


            cv2.imwrite(self.resultName, result)

            try:
                #interface.label.setPixmap(QtGui.QPixmap(os.getcwd() + "/result.bmp"))
                interface.label.setPixmap(QtGui.QPixmap(self.resultName))
            except Exception as e:
                print(e)
            self.finished.emit()
        except:
            (type, value, traceback) = sys.exc_info()
            sys.excepthook(type, value, traceback)
            interface.createButton.setEnabled(True)
            self.finished.emit()


class section_1_Interface(QtWidgets.QWidget, section_1_Ui_Form):
    """
    Subclassing QWidget to define a custom widget which is used to enter parameters to create ellipse defect
    """

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.createDefect_button.clicked.connect(self.create_defect)
        self.show_graph_button.clicked.connect(self.show_graph)
        self.show_graph_button.setEnabled(False)

    def closeEvent(self, event):
        event.ignore()
        mwSection_1_window.hide()

    def create_defect(self):
        MATRIX_CREATOR.making_ellips(self.x_center_edit.value(), self.y_center_edit.value(), self.ellips_a_edit.value(),
                                     self.ellips_b_edit.value(), self.height_edit.value(), self.width_edit.value())
        self.show_graph_button.setEnabled(True)

    def show_graph(self):
        MATRIX_CREATOR.showGraph()


class section_2_Interface(QtWidgets.QWidget, section_2_Ui_Form):
    """
    Subclassing QWidget to define a custom widget which is used to enter parameters to create giperbola defect
    """

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.createDefect_button.clicked.connect(self.create_defect)
        self.show_graph_button.clicked.connect(self.show_graph)
        self.show_graph_button.setEnabled(False)

    def closeEvent(self, event):
        event.ignore()
        mwSection_2_window.hide()

    def create_defect(self):
        MATRIX_CREATOR.making_giperbola(self.x_center_edit.value(), self.y_center_edit.value(),
                                        self.giperbola_a_edit.value(), self.giperbola_b_edit.value(),
                                        self.height_edit.value(), self.width_edit.value())
        self.show_graph_button.setEnabled(True)

    def show_graph(self):
        MATRIX_CREATOR.showGraph()


class section_3_Interface(QtWidgets.QWidget, section_3_Ui_Form):
    """
    Subclassing QWidget to define a custom widget which is used to enter parameters to create pow defect
    """

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.createDefect_button.clicked.connect(self.create_defect)
        self.show_graph_button.clicked.connect(self.show_graph)
        self.show_graph_button.setEnabled(False)

    def closeEvent(self, event):
        event.ignore()
        mwSection_3_window.hide()

    def create_defect(self):
        MATRIX_CREATOR.making_pow(self.parabola_x_edit.value(), self.parabola_y_edit.value(),
                                       self.parabola_stretching_edit.value(), self.parabola_pow_edit.value(), self.height_edit.value(), self.width_edit.value())
        self.show_graph_button.setEnabled(True)

    def show_graph(self):
        MATRIX_CREATOR.showGraph()


class section_4_Interface(QtWidgets.QWidget, section_4_Ui_Form):
    """
    Subclassing QWidget to define a custom widget which is used to enter parameters to create parabaloid defect
    """

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.createDefect_button.clicked.connect(self.create_defect)
        self.show_graph_button.clicked.connect(self.show_graph)
        self.show_graph_button.setEnabled(False)

    def closeEvent(self, event):
        event.ignore()
        mwSection_4_window.hide()

    def create_defect(self):
        MATRIX_CREATOR.making_paraboloid(self.x_center_edit.value(), self.y_center_edit.value(),
                                         self.paraboloid_a_edit.value(), self.paraboloid_b_edit.value(),
                                         self.height_edit.value())
        self.show_graph_button.setEnabled(True)

    def show_graph(self):
        MATRIX_CREATOR.showGraph()


class section_5_Interface(QtWidgets.QWidget, section_5_Ui_Form):
    """
    Subclassing QWidget to define a custom widget which is used to enter parameters to create line defect
    """

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.createDefect_button.clicked.connect(self.create_defect)
        self.show_graph_button.clicked.connect(self.show_graph)
        self.show_graph_button.setEnabled(False)

    def closeEvent(self, event):
        event.ignore()
        mwSection_5_window.hide()

    def create_defect(self):
        MATRIX_CREATOR.making_line(self.line_stretching_edit.value(), self.line_shift_edit.value(),
                                   self.height_edit.value(), self.width_edit.value())
        self.show_graph_button.setEnabled(True)

    def show_graph(self):
        MATRIX_CREATOR.showGraph()


class section_6_Interface(QtWidgets.QWidget, section_6_Ui_Form):
    """
    Subclassing QWidget to define a custom widget which is used to enter parameters to create Math Functions defects
    """

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.createDefect_button.clicked.connect(self.create_defect)
        self.show_graph_button.clicked.connect(self.show_graph)
        self.show_graph_button.setEnabled(False)

    def closeEvent(self, event):
        event.ignore()
        mwSection_6_window.hide()

    def create_defect(self):
        MATRIX_CREATOR.making_func(self.math_Y_Stretching_edit.value(), self.math_X_Stretching_edit.value(),
                                   self.math_X_Shift_edit.value(), self.math_Y_Shift_edit.value(),
                                   self.height_edit.value(), self.width_edit.value(),
                                   self.math_graphic_type_edit.currentText())

        self.show_graph_button.setEnabled(True)

    def show_graph(self):
        MATRIX_CREATOR.showGraph()


class parametersInterface(QtWidgets.QWidget, Ui_Form):
    """
    Subclassing QWidget to define a custom widget which is used to enter parameters for vignette, noise and blur effects
    """

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.blur_coreEdit.lineEdit().setReadOnly(True)

    def closeEvent(self, event):
        event.ignore()
        mwParameters.hide()


class Interface(QtWidgets.QMainWindow, Ui_MainWindow):
    """
    Subclassing QMainWindow to define a custom window which describes my main window
    """

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.createButton.clicked.connect(self.result_pressed)
        self.graphButton.clicked.connect(self.showGraph)
        self.setParametersButton.clicked.connect(self.parameters_pressed)
        self.actionAdd_Deffect.triggered.connect(self.selectDefect)
        self.actionSave_Parameters.triggered.connect(self.saveParameters)
        self.actionLoad_Parameters.triggered.connect(self.loadParameters)
        self.graphButton.setEnabled(False)
        self.createButton.setEnabled(False)
        self.resolutionEdit.lineEdit().setReadOnly(True)

        self.section_1_button_ellipse.clicked.connect(self.show_section_1)
        self.section_2_button_giperbola.clicked.connect(self.show_section_2)
        self.section_3_button_parabola.clicked.connect(self.show_section_3)
        self.section_4_button_paraboloid.clicked.connect(self.show_section_4)
        self.section_5_button_line.clicked.connect(self.show_section_5)
        self.section_6_button_math.clicked.connect(self.show_section_6)


    def closeEvent(self, event):
        event.ignore()
        sys.exit()


    @Slot()
    def on_finish(self):
        """
        Slot responsible for the thread termination event
        """
        self.createButton.setEnabled(True)
        self.graphButton.setEnabled(True)

    @Slot(int)
    def on_progress(self, prg):
        """
        Slot responsible for the progress event
        """
        self.progressBar.setValue(prg)

    def result_pressed(self):
        """
        Slot responsiblу for Create Button
        """

        filter = "Images (*.png *.jpg *.bmp)"
        resultName,_ = QFileDialog.getSaveFileName(None, "Save", "", filter)
        print(resultName)

        self.thread = QThread()
        self.worker = Worker(resultName)
        self.worker.moveToThread(self.thread)
        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.worker.finished.connect(self.on_finish)
        self.worker.progress.connect(self.on_progress)
        self.thread.start()
        self.createButton.setEnabled(False)
        self.graphButton.setEnabled(False)

    def parameters_pressed(self):
        """
        Slot responsiblу for Parameters Button
        """
        mwParameters.show()

    def selectDefect(self):
        """
        Slot responsiblу for Select Defect button
        """
        defectName,_ = QFileDialog.getOpenFileName(interface, "Open Defect", "~", "Matrix File (*.txt)")
        global DEFECT_NAME
        #DEFECT_NAME = Path(defectName[0]).name
        DEFECT_NAME = defectName
        print(DEFECT_NAME)
        self.createButton.setEnabled(True)

    def saveParameters(self):
        """
        Slot responsiblу for Save Parameters button
        """
        with open("program_parameters.ini", "w") as fi:
            for line in interface.findChildren(QSpinBox):
                fi.write(line.objectName() + "=" + str(line.value()) + "\n")
            for line in interface.findChildren(QDoubleSpinBox):
                fi.write(line.objectName() + "=" + str(line.value()) + "\n")

            for line in parameters.findChildren(QSpinBox):
                fi.write(line.objectName() + "=" + str(line.value()) + "\n")
            for line in parameters.findChildren(QDoubleSpinBox):
                fi.write(line.objectName() + "=" + str(line.value()) + "\n")

            fi.close()

    def loadParameters(self):
        """
        Slot responsiblу for Load Parameters button
        """
        settings = QSettings("program_parameters.ini", QSettings.IniFormat)

        for line in interface.findChildren(QSpinBox):
            line.setValue(int(settings.value(line.objectName())))
        for line in interface.findChildren(QDoubleSpinBox):
            line.setValue(float(settings.value(line.objectName())))
        for line in parameters.findChildren(QSpinBox):
            line.setValue(int(settings.value(line.objectName())))
        for line in parameters.findChildren(QDoubleSpinBox):
            line.setValue(float(settings.value(line.objectName())))

    def showGraph(self):
        """
        Slot responsiblу for Show 3D Surface button
        """
        x, y, z = makeData()

        fig = pylab.figure()
        fig.canvas.set_window_title('Surface')
        axes = Axes3D(fig)

        axes.set_xlim3d(0, X_SIZE)
        axes.set_ylim3d(0, Y_SIZE)

        axes.set_xlabel("mm")
        axes.set_xticks([0, X_SIZE * (1 / 3), X_SIZE * (2 / 3), X_SIZE])
        axes.set_xticklabels(["$0$", r"$0.1$", r"$0.2$", r"$0.3$"])

        axes.set_ylabel("mm")
        axes.set_yticks([0, Y_SIZE * (1 / 3), Y_SIZE * (2 / 3), Y_SIZE])
        axes.set_yticklabels(["$0$", r"$0.1$", r"$0.2$", r"$0.3$"])

        axes.set_zlabel("mcm")
        axes.set_zlim3d(-5, 5)
        surf = axes.plot_surface(x, y, z, cmap=cm.coolwarm)

        fig.colorbar(surf, shrink=0.4, aspect=15)
        pylab.show()

    # Slots responsible for creating defect buttons
    def show_section_1(self):
        mwSection_1_window.show()

    def show_section_2(self):
        mwSection_2_window.show()

    def show_section_3(self):
        mwSection_3_window.show()

    def show_section_4(self):
        mwSection_4_window.show()

    def show_section_5(self):
        mwSection_5_window.show()

    def show_section_6(self):
        mwSection_6_window.show()


def create_image(i, j):
    """
    Create image
    :param i: width of image
    :param j: height of image
    :return: image
    """
    image = Image.new("RGB", (i, j), "black")
    return image


def formula_new(x, y, wavelength, mas, angles, angle1, angle2, alf):
    """
    Count intensity of point (x, y)
    (nx1, ny1, nz1) - direction vector when tilting (rotating around OX) vector (0, 0, 1) by angle1
    (nx2, ny2, nz2) - direction vector when the vector (nx1, ny1, nz1) is rotated around OZ by angle2
    :return intensity
    """
    angle1 = math.pi * angle1 / 180
    angle2 = math.pi * angle2 / 180

    nx1 = 0
    ny1 = -math.sin(angle1)
    nz1 = math.cos(angle1)

    nx2 = math.cos(angle2) * nx1 - math.sin(angle2) * ny1
    ny2 = math.sin(angle2) * nx1 + math.cos(angle2) * ny1
    nz2 = nz1

    if nz2 == 0:
        D_X_Y = 0
    else:
        D_X_Y = - (nx2 * (x - X_SIZE / 2) + ny2 * (y - Y_SIZE / 2)) / (X_SIZE / 900 * nz2)

    S_X_Y = mas[x][y] / 1000

    I1 = alf
    I2 = (1 - alf) * (angles[x][y] ** 4)
    res = (I1 + I2 + 2 * math.sqrt(I1 * I2) * math.cos((2 * math.pi * 2 * (S_X_Y + D_X_Y)) / wavelength))

    return res


def make_interf(image):
    """
    Creates an interference picture
    :param image: empty image
    :return: image with interference picture
    """
    mas = [0] * X_SIZE
    for i in range(X_SIZE):
        mas[i] = [0] * Y_SIZE

    with open('output_after_spline.txt') as f:
        mas = [list(map(float, row.split())) for row in f.readlines()]

    pixels = image.load()

    fr = open("angles.txt", "r")
    angles = [list(map(float, fr.readline().split())) for i in range(X_SIZE)]

    alf = interface.alphaEdit.value()
    iMin = min(alf, 1 - 2 * math.sqrt(alf * (1 - alf)))
    iMax = 1 + 2 * math.sqrt(alf * (1 - alf))

    gMin = interface.gMinEdit.value()
    gMax = interface.gMaxEdit.value()
    angle1 = interface.xAngleEdit.value()
    angle2 = interface.yAngleEdit.value()
    wavelength = interface.wavelengthEdit.value() / 1000000

    for x in range(image.size[0]):
        for y in range(image.size[1]):

            if math.sqrt((x - X_SIZE / 2) ** 2 + ((y - Y_SIZE / 2) ** 2)) <= (X_SIZE / 2):

                r = formula_new(x, y, wavelength, mas, angles, angle1, angle2, alf)

                g = (r - iMin) * (gMax - gMin) / (iMax - iMin) + gMin

                pixels[x, y] = (0, int(g), 0)

            else:
                pixels[x, y] = (0, 0, 0)

    #image.save("test.bmp")

    return image


# Noise
def gauss_noise(image, sigma, mu):
    """
    Realizes gaussian noise
    """
    row, col, ch = image.shape
    gauss = np.random.normal(mu, sigma, (row, col, ch))
    gauss = gauss.reshape(row, col, ch)
    for i in range(0, row):
        for j in range(0, col):
            gauss[i][j][0] = 0
            gauss[i][j][2] = 0
    noisy = image + gauss
    return noisy


def make_noise(image):
    """
    Adds noise effect on image
    :param image: image to change
    :return: image with noise effect
    """
    sigma = parameters.noise_sigmaEdit.value()
    mu = parameters.noise_muEdit.value()
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    gauss_image = gauss_noise(image, sigma, mu)
    return gauss_image


# Blur
def blend_with_mask_matrix(src1, src2, mask):
    res_channels = []
    for c in range(0, src1.shape[2]):
        a = src1[:, :, c]
        b = src2[:, :, c]
        m = mask[:, :, c]
        res = cv2.add(
            cv2.multiply(b, cv2.divide(np.full_like(m, 255) - m, 255.0, dtype=cv2.CV_32F), dtype=cv2.CV_32F),
            cv2.multiply(a, cv2.divide(m, 255.0, dtype=cv2.CV_32F), dtype=cv2.CV_32F),
            dtype=cv2.CV_8U)
        res_channels += [res]
    res = cv2.merge(res_channels)
    return res


def radial_blur_image(image):
    """
    Adds radial blur effect on image
    :param image: image to change
    :return: image with radial blur effect
    """
    radius = parameters.blur_radiusEdit.value() * (X_SIZE // 300)
    sigma = parameters.blur_sigmaEdit.value()
    coreValue = parameters.blur_coreEdit.value()

    gaussian_core = (coreValue, coreValue)

    blurred = cv2.GaussianBlur(image, gaussian_core, sigma)

    w, h = image.shape[:2]
    center_x = int(w / 2)
    center_y = int(h / 2)

    circle_mask = np.zeros_like(image)
    cv2.circle(circle_mask, (center_x, center_y), radius, (255, 255, 255), -1)
    cv2.GaussianBlur(circle_mask, (569, 569), 300, dst=circle_mask)

    res = blend_with_mask_matrix(image, blurred, circle_mask)
    return res


def first_blur_image(image):
    """
    Adds blur effect on image
    :param image: image to change
    :return: image with blur effect
    """
    coreValue = 3
    sigma = math.ceil(X_SIZE / 1000)

    gaussian_core = (coreValue, coreValue)

    res = cv2.GaussianBlur(image, gaussian_core, sigma)

    return res


# Vignette
def make_vignette(image):
    """
    Adds vignette effect on image
    :param image: image to change
    :return: image with vignette effect
    """

    cv2.imwrite("for_vignette.bmp", image)
    image = cv2.imread('for_vignette.bmp')
    alpha = parameters.vignette_alphaEdit.value()
    saturation = parameters.vignette_saturationEdit.value()

    height, width = image.shape[:2]

    X_resultant_kernel = cv2.getGaussianKernel(width, alpha * X_SIZE / 2)  # Create gaussian kernel for x
    Y_resultant_kernel = cv2.getGaussianKernel(height, alpha * Y_SIZE / 2)  # Create gaussian kernel for y

    resultant_kernel = Y_resultant_kernel * X_resultant_kernel.T  # Create 2-dim gaussian kernel for x and y

    mask = (alpha * (X_SIZE / 2 - X_SIZE / 18)) * resultant_kernel / np.linalg.norm(resultant_kernel)
    output = np.copy(image)

    for i in range(3):
        output[:, :, i] = output[:, :, i] * mask

    # Convert to hsv for changing saturation
    hsv = cv2.cvtColor(output, cv2.COLOR_BGR2HSV)

    hsv = np.array(hsv, dtype=np.float64)

    # Scale pixel values up or down for channel 1(Saturation)
    hsv[:, :, 1] = hsv[:, :, 1] * saturation
    hsv[:, :, 1][hsv[:, :, 1] > 255] = 255

    # scale pixel values up or down for channel 2(Value)
    hsv[:, :, 2] = hsv[:, :, 2] * saturation
    hsv[:, :, 2][hsv[:, :, 2] > 255] = 255

    hsv = np.array(hsv, dtype=np.uint8)

    output_bright = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
    return output_bright


#Spline
def makeData():
    """
    Smoothing the surface with bicubic spline
    :return: surface points
    """
    settings = QSettings("main_parameters.ini", QSettings.IniFormat)

    noise_min = float(settings.value("noise_min"))
    noise_max = float(settings.value("noise_max"))
    smooth = float(settings.value("smooth"))
    matrix_size = int(settings.value("start_matrix_size"))




    X = np.linspace(0, X_SIZE, matrix_size)
    Y = np.linspace(0, Y_SIZE, matrix_size)

    x, y = np.meshgrid(X, Y)

    try:
        fr = open(DEFECT_NAME, "r")
        zlist = [list(map(float, fr.readline().split())) for i in range(0, matrix_size)]
        fr.close()
    except Exception as e:
        print(e)


    #Add surface noise
    for i in range(matrix_size):
        for j in range(matrix_size):
            zlist[i][j] += random.gauss(noise_min, noise_max)

    z = np.array(zlist)

    f = interpolate.RectBivariateSpline(X, Y, z, kx=3, ky=3, s=smooth)

    Xspline = np.linspace(0, X_SIZE, X_SIZE)
    Yspline = np.linspace(0, Y_SIZE, Y_SIZE)

    Zspline = f(Xspline, Yspline)

    Xsplinegrid, Ysplinegrid = np.meshgrid(Xspline, Yspline)

    return Xsplinegrid, Ysplinegrid, Zspline


def angle_between_vectors(x1, y1, z1, x2, y2, z2):
    """
    Count angle between 2 vectors
    :return: Angle
    """
    #print(str(x1) + " " + str(y1) + " " + str(z1))
    tt = math.sqrt(x1 * x1 + y1 * y1 + z1 * z1) * math.sqrt(x2 * x2 + y2 * y2 + z2 * z2)
    #print(tt)
    ang = abs(x1 * x2 + y1 * y2 + z1 * z2) / tt
    return (ang)


def make_spline():
    """
    Adds artifacts on surface and count normals
    :return: nothing
    """
    x, y, z = makeData()

    add_artef(z)

    res_matrix = open("output_after_spline.txt", "w")
    for i in range(0, X_SIZE):
        for j in range(0, Y_SIZE):
            res_matrix.write(str(z[i][j]) + " ")
        res_matrix.write("\n")
    res_matrix.close()


    file_angels = open("angles.txt", 'w')
    normals = make_normals_new(z)
    #angl = list()
    for yy in range(0, Y_SIZE, 1):
        for xx in range(0, X_SIZE, 1):

            #Calculating the angle between the normal and the XY plane
            current_ang = angle_between_vectors(normals[yy][xx][0], normals[yy][xx][1], normals[yy][xx][2], 0, 0, 1)
            file_angels.write(str(current_ang) + " ")

        file_angels.write("\n")



# Artifacts
def add_artef(z):
    """
    Determines the type of artifact and adds it to the surface

    :param z: original suface
    :return: nothing
    """
    settings = QSettings(os.getcwd() + "\\artefParam\\" + "mainArtef.ini", QSettings.IniFormat)
    quantity = int(settings.value("quantity"))
    print(quantity)

    for i in range(quantity):
        center_x = random.randint(0, X_SIZE)
        center_y = random.randint(0, X_SIZE)
        type = random.randint(0, len(ARTEFACTS_LIST) - 1)

        ARTEFACTS_LIST[type](center_x, center_y, z, X_SIZE)


def make_normals_new(z):
    """
    Calculate normals

    :param z: original surface
    :return: normals

    normals:Matrix of size X_SIZExY_SIZE, each element of which is the normal vector, according to the formula,
            the normal vector at the point - (F '(x), F' (y), F '(z) = -1 (since the function of 2 variables))
    """

    normals = [[[0, 0, -300 / X_SIZE] for i in range(X_SIZE)] for j in range(Y_SIZE)]

    normals_bool = [[False for i in range(X_SIZE)] for j in range(Y_SIZE)]
    for y in range(1, Y_SIZE - 1):
        for x in range(1, X_SIZE - 1):

            # For all points, partial derivatives with respect to x, y
            normals[y][x][0] = (z[y][x + 1] - z[y][x - 1]) / 2
            normals[y][x][1] = (z[y + 1][x] - z[y - 1][x]) / 2
            normals_bool[y][x] = True

    for y in range(1, Y_SIZE - 1):
        # For boundary points of the 1st row x = 0, y = 1, N-2
        normals[y][0][0] = (-3 * z[y][0] + 4 * z[y][1] - z[y][2]) / 2
        normals[y][0][1] = (z[y + 1][0] - z[y - 1][0]) / 2

    for x in range(1, X_SIZE - 1):
        # For boundary points of the 1st row y = 0, x = 1, N-2
        normals[0][x][0] = (z[0][x + 1] - z[0][x - 1]) / 2
        normals[0][x][1] = (-3 * z[0][x] + 4 * z[1][x] - z[2][x]) / 2

    for y in range(1, Y_SIZE - 1):
        # For the boundary points of the last row x = N-1, y = 1, N-2
        normals[y][X_SIZE - 1][0] = (3 * z[y][X_SIZE - 1] - 4 * z[y][X_SIZE - 2] + z[y][X_SIZE - 3]) / 2
        normals[y][X_SIZE - 1][1] = (z[y + 1][X_SIZE - 1] - z[y - 1][X_SIZE - 1]) / 2

    for x in range(1, X_SIZE - 1):
        # For the boundary points of the last row y = N-1, x = 1, N-2
        normals[Y_SIZE - 1][x][0] = (z[Y_SIZE - 1][x + 1] - z[Y_SIZE - 1][x - 1]) / 2
        normals[Y_SIZE - 1][x][1] = (3 * z[Y_SIZE - 1][x] - 4 * z[Y_SIZE - 2][x] + z[Y_SIZE - 3][x]) / 2

    # Corner points
    normals[Y_SIZE - 1][X_SIZE - 1][0] = (3 * z[Y_SIZE - 1][X_SIZE - 1] - 4 * z[Y_SIZE - 1][X_SIZE - 2] + z[Y_SIZE - 1][
        X_SIZE - 3]) / 2
    normals[Y_SIZE - 1][X_SIZE - 1][1] = (3 * z[Y_SIZE - 1][X_SIZE - 1] - 4 * z[Y_SIZE - 2][X_SIZE - 1] + z[Y_SIZE - 3][
        X_SIZE - 1]) / 2

    normals[0][X_SIZE - 1][0] = (3 * z[0][X_SIZE - 1] - 4 * z[Y_SIZE - 1][X_SIZE - 2] + z[Y_SIZE - 1][X_SIZE - 3]) / 2
    normals[0][X_SIZE - 1][1] = (-3 * z[0][X_SIZE - 1] + 4 * z[1][X_SIZE - 1] - z[2][X_SIZE - 1]) / 2

    normals[Y_SIZE - 1][0][0] = (-3 * z[Y_SIZE - 1][0] + 4 * z[Y_SIZE - 1][1] - z[Y_SIZE - 1][2]) / 2
    normals[Y_SIZE - 1][0][1] = (3 * z[Y_SIZE - 1][0] - 4 * z[Y_SIZE - 2][0] + z[Y_SIZE - 3][0]) / 2

    normals[0][0][0] = (-3 * z[0][0] + 4 * z[0][1] - z[0][2]) / 2
    normals[0][0][1] = (-3 * z[0][0] + 4 * z[1][0] - z[2][0]) / 2

    return normals



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    qtmodern.styles.dark(app)

    #warnings.simplefilter("ignore")

    app.setWindowIcon(QtGui.QIcon("logo_png.png"))

    parameters = parametersInterface()
    interface = Interface()
    section_1_window = section_1_Interface()
    section_2_window = section_2_Interface()
    section_3_window = section_3_Interface()
    section_4_window = section_4_Interface()
    section_5_window = section_5_Interface()
    section_6_window = section_6_Interface()

    mwMain = qtmodern.windows.ModernWindow(interface)
    mwParameters = qtmodern.windows.ModernWindow(parameters)
    mwSection_1_window = qtmodern.windows.ModernWindow(section_1_window)
    mwSection_2_window = qtmodern.windows.ModernWindow(section_2_window)
    mwSection_3_window = qtmodern.windows.ModernWindow(section_3_window)
    mwSection_4_window = qtmodern.windows.ModernWindow(section_4_window)
    mwSection_5_window = qtmodern.windows.ModernWindow(section_5_window)
    mwSection_6_window = qtmodern.windows.ModernWindow(section_6_window)

    mwMain.btnMaximize.setEnabled(False)
    mwParameters.btnMaximize.setEnabled(False)
    mwSection_1_window.btnMaximize.setEnabled(False)
    mwSection_2_window.btnMaximize.setEnabled(False)
    mwSection_3_window.btnMaximize.setEnabled(False)
    mwSection_4_window.btnMaximize.setEnabled(False)
    mwSection_5_window.btnMaximize.setEnabled(False)
    mwSection_6_window.btnMaximize.setEnabled(False)


    ###place in center
    mwMain.setGeometry(
        QtWidgets.QStyle.alignedRect(
            PS.QtCore.Qt.LeftToRight,
            PS.QtCore.Qt.AlignCenter,
            mwMain.size(),
            QtGui.QGuiApplication.primaryScreen().availableGeometry(),
        )
    )
    mwParameters.setGeometry(
        QtWidgets.QStyle.alignedRect(
            PS.QtCore.Qt.LeftToRight,
            PS.QtCore.Qt.AlignCenter,
            mwParameters.size(),
            QtGui.QGuiApplication.primaryScreen().availableGeometry(),
        )
    )
    mwSection_1_window.setGeometry(
        QtWidgets.QStyle.alignedRect(
            PS.QtCore.Qt.LeftToRight,
            PS.QtCore.Qt.AlignCenter,
            mwSection_1_window.size(),
            QtGui.QGuiApplication.primaryScreen().availableGeometry(),
        )
    )
    mwSection_2_window.setGeometry(
        QtWidgets.QStyle.alignedRect(
            PS.QtCore.Qt.LeftToRight,
            PS.QtCore.Qt.AlignCenter,
            mwSection_2_window.size(),
            QtGui.QGuiApplication.primaryScreen().availableGeometry(),
        )
    )
    mwSection_3_window.setGeometry(
        QtWidgets.QStyle.alignedRect(
            PS.QtCore.Qt.LeftToRight,
            PS.QtCore.Qt.AlignCenter,
            mwSection_3_window.size(),
            QtGui.QGuiApplication.primaryScreen().availableGeometry(),
        )
    )
    mwSection_4_window.setGeometry(
        QtWidgets.QStyle.alignedRect(
            PS.QtCore.Qt.LeftToRight,
            PS.QtCore.Qt.AlignCenter,
            mwSection_4_window.size(),
            QtGui.QGuiApplication.primaryScreen().availableGeometry(),
        )
    )
    mwSection_5_window.setGeometry(
        QtWidgets.QStyle.alignedRect(
            PS.QtCore.Qt.LeftToRight,
            PS.QtCore.Qt.AlignCenter,
            mwSection_5_window.size(),
            QtGui.QGuiApplication.primaryScreen().availableGeometry(),
        )
    )
    mwSection_6_window.setGeometry(
        QtWidgets.QStyle.alignedRect(
            PS.QtCore.Qt.LeftToRight,
            PS.QtCore.Qt.AlignCenter,
            mwSection_6_window.size(),
            QtGui.QGuiApplication.primaryScreen().availableGeometry(),
        )
    )
    ###


    mwMain.show()
    mwMain.setFixedSize(mwMain.size())

    sys.exit(app.exec_())
