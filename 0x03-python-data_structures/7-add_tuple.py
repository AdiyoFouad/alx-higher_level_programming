#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    la = len(tuple_a)
    lb = len(tuple_b)
# check for tuple_a
    if la < 1:
        tuple_a = (0, 0)
    elif la < 2:
        tuple_a = (tuple_a[0], 0)

# check for tuple_b
    if lb < 1:
        tuple_b = (0, 0)
    elif lb < 2:
        tuple_b = (tuple_b[0], 0)

    r = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    return r
