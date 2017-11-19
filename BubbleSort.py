#!/usr/bin/env python


def BubbleSort(a):
    for i in range(len(a)):
        swaps = 0
        for j in range(len(a)-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                swaps += 1

        if swaps == 0:
            break
    return a


a = [5, 4, 3, 2, 1]
print BubbleSort(a)


