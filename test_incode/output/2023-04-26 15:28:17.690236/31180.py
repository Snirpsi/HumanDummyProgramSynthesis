#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens all ports and multiplyes a list of numbers. """    
    ports = [int(i) for i in sys.argv[1:]]
    ports_sum = 0
    for port in ports:
        ports_sum += port
    print(ports_sum)

<|/ file ext=.py |>