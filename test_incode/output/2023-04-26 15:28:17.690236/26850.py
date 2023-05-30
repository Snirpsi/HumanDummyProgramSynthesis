#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over a port and adds a list of numbers. """    
    port = int(sys.argv[1])
    numbers = []
    for _ in range(port):
        numbers.append(int(sys.argv[2]))
    print(numbers)

<|/ file ext=.py source=github |>