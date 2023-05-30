#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes a list of numbers and removes a port. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python3 remove-numbers-and-port.py <numbers-to-remove> <port-to-remove>")
        sys.exit()
    
    numbers_to_remove = sys.argv[1]
    port_to_remove = sys.argv[2]
    
    numbers_to_remove = numbers_to_remove.split(',')
    
    numbers_to_remove = list(map(int, numbers_to_remove))
    
    port_to_remove = port_to_remove.split(',')
    
    port_to_remove = list(map(int, port_to_remove))
    
    numbers_to_remove.remove