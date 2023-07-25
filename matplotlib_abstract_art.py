from matplotlib import pyplot as plt
from random import randint as rand
from math import sin

waves = 100
height_added = 0.01
frequency_range = 2


def graph(start=-50, end=50, clarity=2, height_added=0.0):
    y = []
    x = []
    sin_frequencies = []
    for _ in range(10):
        sin_frequencies.append(rand(-frequency_range * 100, frequency_range * 100) / 100)
    for i in range(round((start * (30 * clarity))), round((end * (30 * clarity))) + 1):
        n = i / (30 * clarity)
        x.append(n)
        y_total = 0
        for sinewave in sin_frequencies:
            y_total += (sin(n * sinewave) / 3)
        y.append(y_total + height_added)
    return x, y


for j in range(waves):
    points = graph(height_added=j * height_added)
    plt.plot(points[0], points[1])
plt.show()
