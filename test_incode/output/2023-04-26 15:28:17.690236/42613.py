#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a port and returns a list of numbers. """    
    port = int(sys.argv[1]) # Port number
    numbers = []
    for i in range(port):
        numbers.append(i)
    print(numbers)

<|/ file ext=.py source=github |>