#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that multiplyes all ports or multiplyes numbers. """    
    ports = [int(i) for i in sys.argv[1:]]
    ports_multiply = []
    for port in ports:
        ports_multiply.append(port * 2)
    print(ports_multiply)

<|/ file ext=.py filename=