#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that multiplyes a port and adds a list of numbers. """    
    port = int(sys.argv[1])
    numbers = [int(i) for i in sys.argv[2:]]
    numbers = [n*port for n in numbers]
    print(numbers)

<|/ file source=github ext=.py |>