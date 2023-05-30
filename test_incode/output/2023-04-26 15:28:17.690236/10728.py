#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over all ports and opens a list of numbers. """    
    ports = [int(port) for port in sys.argv[1:]]
    
    for port in ports:
        open_list