#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates numbers. """    
    import sys
    
    numbers = []
    for arg in sys.argv[1:]:
        try:
            number = int(arg)
        except ValueError:
            sys.stderr.write('Error: %s is not a valid number\n' % arg)
            sys.exit(1)
        numbers.append(number)
    
    for number in numbers:
        print(number)
        
