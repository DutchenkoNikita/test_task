# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 12:59:51 2022

@author: Okhrimchuk Roman & Maksym Veremchuk
for Sierentz Global Merchants


Test task
"""
import numpy as np


def lucky(temp):
    lucky_arr = np.array([])
    res = np.array([])
    for i in temp:
        if int(i) == 5 or int(i) == 6:
            lucky_arr = np.append(lucky_arr, i)
        else:
            str_res = ''.join(lucky_arr)
            res = np.append(res, str_res)
            lucky_arr = []

    final_res = np.array([])
    for i in range(len(res)):
        if (res[i].count('5') != len(res[i])) and (res[i].count('6') != len(res[i])):
            final_res = np.append(final_res, res[i])

    if final_res.size == 0:
        return 0
    elif len(max(final_res, key=len)) <= 3:
        return 0
    else:
        return max(final_res, key=len)


temp = str(input("Input number for calculation: "))
print(lucky(temp))
