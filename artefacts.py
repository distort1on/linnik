#  Copyright (c) 2021., Illia Popov, All rights reserved.

import random
import math
from PySide2.QtCore import QSettings
import os


#Each function describes artifact type
def artef1(center_x, center_y, z, X_SIZE):
    settings = QSettings(os.getcwd() + "\\artefParam\\" + "artef1.ini", QSettings.IniFormat)

    height = random.uniform(float(settings.value("height_lb")), float(settings.value("height_rb")))
    radius_max = random.uniform(float(settings.value("radius_max_lb")), float(settings.value("radius_max_rb"))) * (X_SIZE / 300)
    radius_min = random.uniform(float(settings.value("radius_min_lb")), float(settings.value("radius_min_rb"))) * (X_SIZE / 300)

    for fi in range(0, 360, 1):
        for i in range(1):
            fi_rad = fi * math.pi / 180
            r = random.uniform(radius_min, radius_max)
            ro = 2 * r * math.cos(1 + fi_rad)
            xx = round(ro * math.cos(fi_rad))
            yy = round(ro * math.sin(fi_rad))
            if (0 <= center_x + xx < X_SIZE and 0 <= center_y + yy < X_SIZE):
                z[center_y + yy][center_x + xx] = height + random.gauss(0, 0.007)

def artef2(center_x, center_y, z, X_SIZE):
    settings = QSettings(os.getcwd() + "\\artefParam\\" + "artef2.ini", QSettings.IniFormat)

    height = random.uniform(float(settings.value("height_lb")), float(settings.value("height_rb")))
    radius_max = random.uniform(float(settings.value("radius_max_lb")), float(settings.value("radius_max_rb"))) * (
                X_SIZE / 300)
    radius_min = random.uniform(float(settings.value("radius_min_lb")), float(settings.value("radius_min_rb"))) * (
                X_SIZE / 300)
    max_gr = random.randint(int(settings.value("max_gr_lb")), int(settings.value("max_gr_rb")))


    for fi in range(0, max_gr, 1):
        for i in range(1):
            fi_rad = fi * math.pi / 180
            r = random.uniform(radius_min, radius_max)
            ro = r
            xx = round(ro * math.cos(fi_rad))
            yy = round(ro * math.sin(fi_rad))
            if (0 <= center_x + xx < X_SIZE and 0 <= center_y + yy < X_SIZE):
                z[center_y + yy][center_x + xx] = height + random.gauss(0, 0.007)


def artef3(X_Center, Y_Center, z, X_SIZE):
    settings = QSettings(os.getcwd() + "\\artefParam\\" + "artef3.ini", QSettings.IniFormat)

    height = random.uniform(float(settings.value("height_lb")), float(settings.value("height_rb")))
    Paraboloid_A = random.uniform(float(settings.value("paraboloid_a_lb")), float(settings.value("paraboloid_a_rb"))) * (X_SIZE / 300)
    Paraboloid_B = random.uniform(float(settings.value("paraboloid_b_lb")), float(settings.value("paraboloid_b_rb"))) * (X_SIZE / 300)
    n = X_SIZE

    for xx in range (round(X_Center - Paraboloid_A), round(X_Center + Paraboloid_A)):
        for yy in range (round(Y_Center - Paraboloid_B), round(Y_Center + Paraboloid_B)):

            ll = ((xx - X_Center)**2)/(Paraboloid_A**2) + ((yy - Y_Center)**2)/(Paraboloid_B**2)
            if ll <= 1 and 0 <= xx < n and 0 <= yy < n:
                if height < 0:
                    z[xx][yy] = 1*(abs(height)*ll + height)
                else:
                    z[xx][yy] = 1*(abs(height)*(-ll) + height)


artef_list = [artef1, artef2, artef3]