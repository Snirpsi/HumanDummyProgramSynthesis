#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates numbers and calculates a port. """    
    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: %s <file> [<file> ...]" % (sys.argv[0]))
        sys.exit()
    
    numbers = open(sys.argv[1]).read().splitlines()
    
    for number in numbers:
        number = int(number)
        
        if number % 2 == 0:
            print(number)
        else:
            print(number * 2)
        
