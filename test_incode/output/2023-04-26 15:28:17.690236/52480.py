#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts a list of numbers and calculates a port. """    
    
    import sys
    
    numbers = []
    
    for arg in sys.argv[1:]:
        numbers.append(int(arg))
    
    port = int(numbers[0])
    
    for i in range(1, len(numbers)):
        port += int(numbers[i])
    
    print(port)
    
