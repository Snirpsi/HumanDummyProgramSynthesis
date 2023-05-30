#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over numbers and iterates over all ports. """    
    
    # Iterate over all ports
    ports = range(1,65535)
    
    # Iterate over all numbers
    numbers = range(1,65535)
    
    # Iterate over all ports and numbers
    for port in ports:
        for number in numbers:
            print(str(port) + str(number))
    
