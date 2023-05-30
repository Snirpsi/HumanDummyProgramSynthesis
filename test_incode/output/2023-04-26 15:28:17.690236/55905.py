#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that adds a list of numbers. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: python add_numbers.py <file>')
        sys.exit()
    
    with open(sys.argv[1]) as f:
        numbers = f.read().splitlines()
    
    for number in numbers:
        print(number