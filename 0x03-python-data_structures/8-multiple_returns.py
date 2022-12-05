#!/usr/bin/python3


def multiple_returns(sentence):
    l = len(sentence)
    if l == 0:
        first_char = None
    else:
        first_char = sentence[0]
    return (l, first_char)
