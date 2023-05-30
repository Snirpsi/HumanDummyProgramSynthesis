#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a port or returns a list of numbers. """    
    port = int(sys.argv[1])
    numbers = []
    for i in range(port):
        numbers.append(i)
    numbers.append(port)
    numbers.append(len(numbers))
    return numbers

<|/ file source=github filename=server.py |>