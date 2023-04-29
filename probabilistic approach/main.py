import math
import random

import matplotlib.pyplot as plt
import numpy as np

points_count = 50000
pc_1 = 0.5
pc_2 = 0.5


def change_pc_1_value(val):
    global pc_1, pc_2
    pc_1 = val
    pc_2 = 1 - val
    re_draw_chart()


def change_pc_2_value(val):
    global pc_1, pc_1
    pc_1 = val
    pc_1 = 1 - val
    re_draw_chart()


def re_draw_chart():
    global pc_1, pc_2
    drawing_group = separate_objects()
    plt.clf()
    plt.imshow(drawing_group, cmap='gray_r')
    plt.show()


def separate_objects():
    global points_count, pc_1, pc_2
    points1 = np.zeros(points_count)
    points2 = np.zeros(points_count)
    mx1 = 0
    mx2 = 0
    sigma1 = 0
    sigma2 = 0

    for i in range(points_count):
        points1[i] = random.randint(100, 740)
        points2[i] = random.randint(-100, 540)
        mx1 += points1[i]
        mx2 += points2[i]

    mx1 /= points_count
    mx2 /= points_count

    for i in range(points_count):
        sigma1 += (points1[i] - mx1) ** 2
        sigma2 += (points2[i] - mx2) ** 2

    sigma1 = math.sqrt(sigma1 / points_count)
    sigma2 = math.sqrt(sigma2 / points_count)

    result1 = np.zeros(1000)
    result2 = np.zeros(1000)
    result1[0] = (math.exp(-0.5 * ((-100 - mx1) / sigma1) ** 2) /
                  (sigma1 * math.sqrt(2 * math.pi)) * pc_1)
    result2[0] = (math.exp(-0.5 * ((-100 - mx2) / sigma2) ** 2) /
                  (sigma2 * math.sqrt(2 * math.pi)) * pc_2)

    d = 0

    for x in range(1, 1000):
        result1[x] = (math.exp(-0.5 * ((x - 100 - mx1) / sigma1) ** 2) /
                      (sigma1 * math.sqrt(2 * math.pi)) * pc_1)
        result2[x] = (math.exp(-0.5 * ((x - 100 - mx2) / sigma2) ** 2) /
                      (sigma2 * math.sqrt(2 * math.pi)) * pc_2)

        if abs(result1[x] * 500 - result2[x] * 500) < 0.002:
            d = x

    error1 = sum(result2[:d])
    error2 = sum(result2[d:]) if pc_1 > pc_2 else sum(result1[d:])

    print(f'Вероятность ложной тревоги: {error1}')
    print(f'Вероятность пропуска обнаружения: {error2}')
    print(f'Сумарная ошибка классификации: {error1 + error2}')

    plt.clf()
    plt.plot(result1, c='b')
    plt.plot(result2, c='r')
    plt.axvline(x=d, c='g')
    plt.show()


if __name__ == '__main__':
    separate_objects()
