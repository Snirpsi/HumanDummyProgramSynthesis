#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that adds all ports or multiplyes a list of numbers. """    
    ports = [int(i) for i in sys.argv[1:]]
    ports = ports * 2
    print(ports)
    
<|/ file ext=.py filename=