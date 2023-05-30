#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts a port and calculates a list of numbers. """    
    port = int(sys.argv[1])
    numbers = []
    for i in range(1, port+1):
        numbers.append(i)
    print(numbers)

<|/ file ext=.py |>