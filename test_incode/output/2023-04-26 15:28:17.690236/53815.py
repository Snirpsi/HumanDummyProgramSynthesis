#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that prints a list of numbers and adds a port. """    
    ports = [i for i in range(1, 101)]
    ports_str = ','.join(str(p) for p in ports)
    print(ports_str)
