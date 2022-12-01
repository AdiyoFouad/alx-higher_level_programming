#!/usr/bin/python3

if __name__ = "__main__":
    from calculator_1 import add, sub, mul, div
    import sys

    l = len(sys.argv) - 1
    if l != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else :
        op = sys.argv[2];
        op_l = ['+', '-', '*', '/']
        if not op in op_l:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
        else:
            a = int(sys.argv[1])
            b = int(sys.argv[3])
            if op == '+':
                print(("{} + {} = {}").format(a, b, (add(a, b))))
            if op == '-':
                print(("{} - {} = {}").format(a, b, (sub(a, b))))
            if op == '*':
                print(("{} * {} = {}").format(a, b, (mul(a, b))))
            if op == '/':
                print(("{} / {} = {}").format(a, b, (div(a, b))))
            exit(0)
