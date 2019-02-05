# -*- coding: utf-8 -*-

def partion(array, low, high):
    key = array[low]
    while low < high:
        while low < high and array[high] >= key:
            high -= 1
        if low < high:
            array[low] = array[high]
        while low < high and array[low] > key:
            low += 1
        if low < high:
            array[high] = array[low]
    array[low] = key
    return low


def quick_sort(array, low, high):
    if low < high:
        key_index = partion(array, low, high)
        quick_sort(array, low, key_index)
        quick_sort(array, key_index + 1, high)


def sub_sort(array, low, high):
    key = array[low]
    while low < high:
        while low < high and array[high] >= key:
            high -= 1
        while low < high and array[high] < key:
            array[low] = array[high]
            low += 1
            array[high] = array[low]
    array[low] = key
    return low


def quick_sort1(array, low, high):
    if low < high:
        key_index = sub_sort(array, low, high)
        quick_sort1(array, low, key_index)
        quick_sort1(array, key_index + 1, high)
