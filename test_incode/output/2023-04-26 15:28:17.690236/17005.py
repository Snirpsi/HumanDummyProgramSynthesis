#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates numbers and enumerates a port. """    
    
    import sys
    
    port = int(sys.argv[1])
    
    numbers = range(port)
    
    enumerated_numbers = enumerate(numbers)
    
    for number, enumerated_number in enumerated_numbers:
        print(number, enumerated_number)
    
