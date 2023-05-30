#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes numbers and stores a list of numbers. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python remove_numbers.py <filename>")
        sys.exit()
    
    filename = sys.argv[1]
    
    with open(filename, 'r') as file:
        numbers = file.read().splitlines()
    
    numbers = [int(i) for i in numbers]
    
    numbers = [i for i in numbers if not (i in 