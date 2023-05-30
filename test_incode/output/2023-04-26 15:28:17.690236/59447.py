#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes all ports and calculates a list of numbers. """    
    
    ports = removePorts()
    
    numbers = calculateNumbers(ports)
    
    print(numbers)
    
