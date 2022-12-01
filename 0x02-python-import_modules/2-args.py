#!/usr/bin/python3
if __name__ == "__main__":
    """Print the number of and list of arguments."""
    import sys

    lenght = len(sys.argv) - 1
    if lenght == 0:
        print("0 arguments.")
    elif lenght == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(lenght))
    for index in range(lenght):
        print("{}: {}".format(index + 1, sys.argv[index + 1]))
