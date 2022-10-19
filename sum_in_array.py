# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 12:59:22 2022

@author: Okhrimchuk Roman & Maksym Veremchuk
for Sierentz Global Merchants


Test task
"""
import numpy as np


def find_sum(arr, res):
    arr.sort()
    final_arr = np.array([])
    start, end = 0, arr.size - 1
    while start < end:
        temp_res = arr[start] + arr[end]
        if temp_res == res:
            final_arr = np.append(final_arr, [arr[start], arr[end]])
            start += 1
            end -= 1
        elif temp_res < res:
            start += 1
        else:
            end -= 1
    if final_arr.size == 0:
        return -1
    return final_arr

arr_1 = np.array([-3, 1, 4, 6])

print(find_sum(arr_1, 7))
