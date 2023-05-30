#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens numbers. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s number" % sys.argv[0])
        exit(1)
    
    numbers = sys.argv[1:]
    
    for number in numbers:
        try:
            number = int(number)
        except ValueError:
            print("Invalid number: %s" % number)
            continue
        
        print("