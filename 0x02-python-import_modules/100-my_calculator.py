#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys

    lenght = len(sys.argv) - 1
    if lenght != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        op = sys.argv[2]
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        if op == '+':
            print("{} + {} = {}".format(a, b, (add(a, b))))
        elif op == '-':
            print("{} - {} = {}".format(a, b, (sub(a, b))))
        elif op == '*':
            print("{} * {} = {}".format(a, b, (mul(a, b))))
        elif op == '/':
            print("{} / {} = {}".format(a, b, (div(a, b))))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
        exit(0)
