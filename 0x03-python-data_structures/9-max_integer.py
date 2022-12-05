#!/usr/bin/python3


def max_integer(my_list=[]):
    if my_list == []:
        return None
    my_list.sort()
    big = my_list[(len(my_list) - 1)]
    return big
