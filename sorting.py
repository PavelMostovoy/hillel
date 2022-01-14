"""
sorting examples
"""
import time
import random


def timing(func):
    def inner(*args):
        start = time.time()
        func(*args)
        print(f"{func.__name__}  Run time: {time.time() - start}")
    return inner


# Bubble Sort Algorithm
@timing
def bubble_sort(data):
    length = len(data)
    for i_index in range(length):
        need_sorting = False  # add check for sorting complete
        for j_index in range(0, length - i_index - 1):
            if data[j_index] > data[j_index + 1]:
                data[j_index], data[j_index + 1] = data[j_index + 1], data[
                    j_index]
                need_sorting = True
        if not need_sorting:
            break
    print(data)


# Insertion Sort Algorithm
@timing
def selection_sort(data):
    for scan_index in range(0, len(data)):
        min_index = scan_index
        for comp_index in range(scan_index + 1, len(data)):
            if data[comp_index] < data[min_index]:
                min_index = comp_index
        if min_index != scan_index:
            data[scan_index], data[min_index]=data[min_index], data[scan_index]
    print(data)


# Quick Sort Algorithm

def quick_sort(data, left, right):
    """
    data : data
    left: begin of sorting
    right: end of sorting
    """
    if right <= left:
        return
    else:
        pivot = partition(data, left, right)
        quick_sort(data, left, pivot - 1)
        quick_sort(data, pivot + 1, right)
    return data


def partition(data, left, right):
    """This function chooses a pivot point that dertermines the left and
    right side of the sort"""
    pivot = data[left]
    left_index = left + 1
    right_index = right

    while True:
        while left_index <= right_index and data[left_index] <= pivot:
            left_index += 1
        while right_index >= left_index and data[right_index] >= pivot:
            right_index -= 1
        if right_index <= left_index:
            break
        data[left_index], data[right_index] = data[right_index], data[left_index]
        # print(data)

    data[left], data[right_index] = data[right_index], data[left]
    # print(data)
    return right_index



data = [random.randint(0, 10000) for _ in range(10_000)]
l1 = data.copy()
l2 = data.copy()
l3 = data.copy()


start = time.time()
l1.sort()
print(l1)
print(time.time()-start)

selection_sort(l2)

bubble_sort(l3)

