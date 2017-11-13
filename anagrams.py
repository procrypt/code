#!/usr/bin/env python

a = raw_input()
b = raw_input()


def anagram(a, b):
    A = list(a)
    B = list(b)
    counter = 0

    for i in A:
        for j in B:
            if i == j:
                counter += 2    # Two because it is in list A and B
                B.remove(j)     # remove it from the list
                break

    return len(a)+len(b)-counter

print anagram(a, b)