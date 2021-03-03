#  Copyright (c) 2021, Illia Popov. All rights reserved.

import math
import matplotlib
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
import numpy
import pylab
matplotlib.use("Qt5Agg")

def ost(a, k):

    if (a < 0):
        return 0
    a = a % 1
    for i in range(0, k):
        if (i/k <= a <= (i+1)/k):
            return i




def making_paraboloid(X_Center, Y_Center, Paraboloid_A, Paraboloid_B, height):
    k = 200
    n = 60
    z = [[0] * n for i in range(0, n)]



    for xx in range (round(X_Center*k - Paraboloid_A*k), round(X_Center*k + Paraboloid_A*k)):
        for yy in range (round(Y_Center*k - Paraboloid_B*k), round(Y_Center*k + Paraboloid_B*k)):
            x, y = xx/k, yy/k
            ll = ((x - X_Center)**2)/(Paraboloid_A**2) + ((y - Y_Center)**2)/(Paraboloid_B**2)
            if ll <= 1 and 0 <= xx <= n and 0 <= yy <= n:
                if height < 0:
                    z[xx][yy] = 1*(abs(height)*ll + height)
                else:
                    z[xx][yy] = 1*(abs(height)*(-ll) + height)

    create_matrix(z, n)


def making_line(Stretching, Shift, height, width):
    k = 200
    n = 60
    z = [[0] * n for i in range(0, n)]

    X_Start = 0
    X_End = 0.3
    scratch_or_crack = 0

    X_Start = round(X_Start * k); X_End = round(X_End * k);
    for xx in range(X_Start, X_End):

        x = xx/k


        y = x * Stretching + Shift


        yy = math.floor(y)*k + ost(y, k)


        delta_height = 0
        if (scratch_or_crack == 0):

            delta_height = height/(k*width//2)


        cur_height = height
        i = 0
        while (i < (k*width-1)//2+1 ):
            if (0 <= (yy + i) < n):
                z[yy+i][xx] = cur_height
            if (0 <= (yy - i) < n):
                z[yy-i][xx] = cur_height
            cur_height -= delta_height
            i += 1

    create_matrix(z, n)


def making_parabola(Parabola_A, Parabola_B, Parabola_C, height, width):
    k = 200
    n = 60
    z = [[0] * n for i in range(0, n)]

    X_Start = 0
    X_End = 0.3
    scratch_or_crack = 0


    X_Start = round(X_Start * k); X_End = round(X_End * k);
    for xx in range(X_Start, X_End):

        x = xx/k


        y = x * x * Parabola_A + x * Parabola_B + Parabola_C


        yy = math.floor(y)*k + ost(y, k)


        delta_height = 0
        if (scratch_or_crack == 0):

            delta_height = height/(k*width//2)


        cur_height = height
        i = 0
        while i < (k*width-1)//2+1:
            if (0 <= (yy + i) < n):
                z[yy+i][xx] = cur_height
            if (0 <= (yy - i) < n):
                z[yy-i][xx] = cur_height
            cur_height -= delta_height
            i += 1

    create_matrix(z, n)


def making_ellips(X_Center, Y_Center, Ellips_A, Ellips_B, height, width):
    k = 200
    n = 60
    z = [[0] * n for i in range(0, n)]

    X_Start = 0
    X_End = 0.3
    scratch_or_crack = 0


    X_Start = round(X_Start * k); X_End = round(X_End * k);
    for xx in range(X_Start, X_End):

        x = xx/k


        ll = Ellips_B*Ellips_B*(1 - ((x - X_Center)*(x - X_Center))/(Ellips_A * Ellips_A))
        if (ll < 0):
            continue
        y1 = math.sqrt(ll) + Y_Center
        y2 = -math.sqrt(ll) + Y_Center


        yy1 = math.floor(y1) * k + ost(y1, k)
        yy2 = math.floor(y2) * k + ost(y2, k)


        delta_height = 0
        if (scratch_or_crack == 0):

            delta_height = height/(k*width//2)


        cur_height = height
        i = 0
        while i < (k * width - 1) // 2 + 1:
            if (0 <= (yy1 + i) < n):
                z[yy1+i][xx] = cur_height
            if (0 <= (yy1 - i) < n):
                z[yy1-i][xx] = cur_height
            if (0 <= (yy2 + i) < n):
                z[yy2+i][xx] = cur_height
            if (0 <= (yy2 - i) < n):
                z[yy2-i][xx] = cur_height
            cur_height -= delta_height
            i += 1

    create_matrix(z, n)


def making_giperbola(X_Center, Y_Center, Giperbola_A, Giperbola_B, height, width):
    k = 200
    n = 60
    z = [[0] * n for i in range(0, n)]

    X_Start = 0
    X_End = 0.3
    scratch_or_crack = 0

    X_Start = round(X_Start * k); X_End = round(X_End * k);
    for xx in range(X_Start, X_End):

        x = xx/k


        ll = Giperbola_B * Giperbola_B*(- 1 + ((x - X_Center)*(x - X_Center)) / (Giperbola_A * Giperbola_A))
        if (ll < 0):
            continue

        y = math.sqrt(ll) + Y_Center


        yy = math.floor(y)*k + ost(y, k)


        delta_height = 0
        if (scratch_or_crack == 0):

            delta_height = height/(k*width//2)


        cur_height = height
        i = 0
        while i < (k * width - 1) // 2 + 1:
            if (0 <= (yy + i) < n):
                z[yy+i][xx] = cur_height
            if (0 <= (yy - i) < n):
                z[yy-i][xx] = cur_height
            cur_height -= delta_height
            i += 1

    create_matrix(z, n)




def making_func(Y_Stretching, X_Stretching, X_Shift, Y_Shift, height, width, graphic_type):
    k = 200
    n = 60
    z = [[0] * n for i in range(0, n)]

    X_Start = 0
    X_End = 0.3
    scratch_or_crack = 0

    X_Start = round(X_Start * k); X_End = round(X_End * k);
    for xx in range(X_Start, X_End):

        x = xx/k


        if (graphic_type == "sin"):
            y = (Y_Stretching * math.sin(X_Stretching * x + X_Shift) + Y_Shift)
        elif (graphic_type == "tan"):
            y = (Y_Stretching * math.tan(X_Stretching * x + X_Shift) + Y_Shift)
        elif (graphic_type == "atan" ):
            y = (Y_Stretching * math.atan(X_Stretching * x + X_Shift) + Y_Shift)
        elif (graphic_type == "exp"):
            y = (Y_Stretching * math.exp(X_Stretching * x + X_Shift) + Y_Shift)
        elif (graphic_type == "ln" and X_Stretching * x + X_Shift > 0):
            y = (Y_Stretching * math.log(X_Stretching * x + X_Shift) + Y_Shift)
        else:
            continue


        yy = math.floor(y)*k + ost(y, k)



        delta_height = 0
        if (scratch_or_crack == 0):

            delta_height = height/(k*width//2)


        cur_height = height
        i = 0
        while i < (k * width - 1) // 2 + 1:
            if (0 <= (yy + i) < n):
                z[yy+i][xx] = cur_height
            if (0 <= (yy - i) < n):
                z[yy-i][xx] = cur_height
            cur_height -= delta_height
            i += 1

    create_matrix(z, n)




def create_matrix(z, n):
    fw = open("dem_created.txt", "w")
    for i in range(0, n):
        for j in range(0, n):
            fw.write(str(z[i][j]) + " ")
        fw.write("\n")
    fw.close()

def showGraph():
    n = 60

    fr = open("dem_created.txt", "r")
    z = [list(map(float, fr.readline().split())) for i in range(0, n)]
    fr.close()

    x = numpy.arange(0, n, 1)
    y = numpy.arange(0, n, 1)





    xgrid, ygrid = numpy.meshgrid(x, y)
    zgrid = numpy.array(z)

    fig = pylab.figure()
    fig.canvas.set_window_title('Surface')
    axes = Axes3D(fig)

    axes.set_xlim3d(0, n)
    axes.set_ylim3d(0, n)

    axes.set_xlabel("mm")
    axes.set_xticks([0, n * (1 / 3), n * (2 / 3), n])
    axes.set_xticklabels(["$0$", r"$0.1$", r"$0.2$", r"$0.3$"])

    axes.set_ylabel("mm")
    axes.set_yticks([0, n * (1 / 3), n * (2 / 3), n])
    axes.set_yticklabels(["$0$", r"$0.1$", r"$0.2$", r"$0.3$"])

    axes.set_zlabel("mcm")
    axes.set_zlim3d(-5, 5)
    surf = axes.plot_surface(xgrid, ygrid, zgrid, cmap=cm.coolwarm)

    fig.colorbar(surf, shrink=0.4, aspect=15)
    pylab.show()



