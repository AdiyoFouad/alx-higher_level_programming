#!/usr/bin/python3


def divisible_by_2(my_list=[]):
    copy = my_list.copy()
    for a in range(len(copy)):
        if copy[a] % 2 == 0:
            copy[a] = True
        else:
            copy[a] = False
    return copy
