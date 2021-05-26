import random
import string

import numpy as np
import scipy.integrate as integrate
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from math import *
import subprocess
import PySimpleGUI as sg


def solve(n, points):
    f = open("C:\\Users\\38067\\Desktop\\ogkg\\bin\\Debug\\input.txt", "w")
    f.write(str(n) + "\n")
    x = []
    y = []
    for p in points:
        f.write(str(p[0]) + " " + str(p[1]) + "\n")
        x.append(p[0])
        y.append(p[1])
    f.close()

    cmd = "C:\\Users\\38067\\Desktop\\ogkg\\bin\\Debug\\ogkg.exe"
    subprocess.call(cmd)

    f = open("C:\\Users\\38067\\Desktop\\ogkg\\bin\\Debug\\output.txt", "r")
    pair = []
    for i in range(n):
        pair.append(int(f.readline()))
    f.close()
    print(pair)

    plt.scatter(x, y)
    for i in range(n):
        plt.plot([x[i], x[pair[i]]], [y[i], y[pair[i]]])
    plt.show()


layout = [
    [
        sg.Button("Ручне введення")
    ],
    [
        sg.Button("Автогенерація")
    ],
]

window = sg.Window("Найближчі точки", layout)

# Create an event loop
while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == "Ручне введення":
        layout = [
            [
                sg.Text("n = "),
                sg.In(size=(5, 1), enable_events=True, key="n", default_text="2"),
            ],
            [
                sg.Text("Точки")
            ],
            [
                sg.Multiline(autoscroll=True, size=(10, 10), enable_events=True, key="points", default_text="1 1\n2 3"),
            ],
            [
                sg.Button("Порахувати")
            ],
        ]
        window.close()
        window = sg.Window("Найближчі точки", layout)

    if event == "Автогенерація":
        layout = [
            [
                sg.Text("n = "),
                sg.In(size=(5, 1), enable_events=True, key="n", default_text="2"),
            ],
            [
                sg.Button("Порахувати")
            ],
        ]
        window.close()
        window = sg.Window("Найближчі точки", layout)

    if event == "Порахувати":
        n = int(values["n"])
        points = []

        if "points" in values:
            coordinates = values["points"].split()
            for i in range(1, len(coordinates), 2):
                points.append([coordinates[i-1], coordinates[i]])
        else:
            for i in range(n):
                points.append([random.randint(0, 100000), random.randint(0, 100000)])

        solve(n, points)

        layout = [
            [
                sg.Button("Ручне введення")
            ],
            [
                sg.Button("Автогенерація")
            ],
        ]
        window.close()
        window = sg.Window("Найближчі точки", layout)

