import matplotlib.pyplot as plt
import numpy as np

# Initial variables
txt_file = "G:/Edgar Dobra/GPC Samples/03.01.2024_OT2_PS-b-PLA_PS-b-PLA.txt"
color_palette = 2
RI_calibration = "./RI Calibration curve.txt"
x_lim = [1e3, 1e8]
y_lim = [0, 1.2]
brush_from = 1e5


file = open(txt_file, "r")
content = file.readlines()
file.close()
list_content = []
for row in content:
    list_content.append(row.strip("\n").split("\t"))
data_array = np.array(list_content)

file_RI = open(RI_calibration, "r")
content_RI = file_RI.readlines()
file_RI.close()
list_content_RI = []
for row in content_RI:
    list_content_RI.append(row.strip("\n").split("\t"))
data_array_RI = np.array(list_content_RI)


def color(number):
    if color_palette == 1:
        if number == 0:
            return "#FA7921"
        elif number == 1:
            return "#5BC0EB"
        elif number == 2:
            return "#E55934"
        elif number == 3:
            return "#9BC53D"
        elif number == 4:
            return "#4059AD"
        elif number == 5:
            return "#037171"
        elif number == 6:
            return "#FF3562"

    elif color_palette == 2:
        if number == 0:
            return "#A4036F"
        elif number == 1:
            return "#048BA8"
        elif number == 2:
            return "#16DB93"
        elif number == 3:
            return "#F29E4C"
        elif number == 4:
            return "#EFEA5A"
        elif number == 5:
            return "#A18276"

    elif color_palette == 11:
        if number == 0:
            return "#FA7921"
        elif number == 1:
            return "#5BC0EB"
    elif color_palette == 12:
        if number == 0:
            return "#E55934"
        elif number == 1:
            return "#9BC53D"
    elif color_palette == 13:
        if number == 0:
            return "#4059AD"
        elif number == 1:
            return "#037171"
    elif color_palette == 14:
        if number == 0:
            return "#A4036F"
        elif number == 1:
            return "#048BA8"
    elif color_palette == 15:
        if number == 0:
            return "#16DB93"
        elif number == 1:
            return "#F29E4C"
    elif color_palette == 16:
        if number == 0:
            return "#EFEA5A"
        elif number == 1:
            return "#A18276"
    elif color_palette == 17:
        if number == 0:
            return "#C5D86D"
        elif number == 1:
            return "#0D1321"
    elif color_palette == 18:
        if number == 0:
            return "#42113C"
        elif number == 1:
            return "#6BD425"
    elif color_palette == 19:
        if number == 0:
            return "#663F46"
        elif number == 1:
            return "#3C362A"
    elif color_palette == 20:
        if number == 0:
            return "#6874E8"
        elif number == 1:
            return "#F7ACCF"


def max_of_y_within_range(x_array, y_array):
    mask = np.logical_and(x_array > brush_from, x_array < 1e8)
    return np.max(y_array[mask])


def min_of_y_within_range(x_array, y_array):
    mask = np.logical_and(x_array > 1e3, x_array < 1e4)
    return np.min(y_array[mask])


def get_data(index):
    x_a = np.delete(data_array_RI[:, 1], [0, 1], 0)
    x_a = x_a.astype(float)
    x_a = 10**x_a
    y_a = np.delete(data_array[:, index * 2 + 1], [0, 1], 0).astype(float)

    min_y = min_of_y_within_range(x_a, y_a)
    for value in range(len(y_a)):
        y_a[value] = y_a[value] - min_y

    max_y = max_of_y_within_range(x_a, y_a)
    for value in range(len(y_a)):
        y_a[value] = y_a[value] / max_y

    return x_a, y_a


for i in range(int(len(data_array[0, :])/2)):
    x = get_data(i)[0]
    y = get_data(i)[1]
    plt.plot(x, y, color(i), label=data_array[0, 2*i])


plt.xscale("log")
ax = plt.gca()
ax.set_xlim(x_lim)
ax.set_ylim(y_lim)
plt.xlabel("Molecular weight (g/mol)")
plt.ylabel("Normalization")
plt.legend()
plt.show()
