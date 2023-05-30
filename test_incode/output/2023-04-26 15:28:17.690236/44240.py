#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts numbers. """    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <number> [<number> ...]" % sys.argv[0])
        sys.exit()
    
    numbers = sys.argv[1:]
    
    for number in numbers:
        print(convert_number(number))
        
    
