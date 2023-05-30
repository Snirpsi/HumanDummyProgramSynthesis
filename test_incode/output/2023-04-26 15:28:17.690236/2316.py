#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that removes numbers. """    
    numbers = input().split()
    numbers = list(map(int, numbers))
    numbers.sort()
    numbers.reverse()
    print(" ".join(map(str, numbers)))

<|/ file filename=remove-numbers.py source=github |>