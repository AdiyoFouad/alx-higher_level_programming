#!/usr/bin/python3
if __name__ == "__main__":
    import sys
l = len(sys.argv) - 1
sum = 0
if l == 0:
    print("0")
else:
    for i in range(l):
        sum += int(sys.argv[i + 1])
    print(("{}").format(sum))
