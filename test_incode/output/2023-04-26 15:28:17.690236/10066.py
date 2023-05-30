#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts all ports and multiplyes numbers. """    
    ports = [int(i) for i in sys.argv[1:]]
    ports = [i * 2 for i in ports]
    print(ports)

<|/ file source=github ext=.py filename=port