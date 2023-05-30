#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints numbers or converts a list of numbers. """    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: python list.py <numbers>')
        sys.exit()
    
    numbers = sys.argv[1:]
    
    i = 0
    while i < len(numbers):
        if numbers[i] == '':
            numbers.pop(i)
            