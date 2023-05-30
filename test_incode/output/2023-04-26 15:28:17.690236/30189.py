#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over a list of numbers or enumerates numbers. """    
    
    import sys
    
    # Read command line arguments
    args = sys.argv[1:]
    
    # Parse command line arguments
    numbers = []
    for arg in args:
        try:
            numbers.append(int(arg))
        except ValueError:
            print('Invalid number: {}'.format(arg))
    
    # Print numbers
    for number in numbers:
        print('{}: {}'.format(number, 