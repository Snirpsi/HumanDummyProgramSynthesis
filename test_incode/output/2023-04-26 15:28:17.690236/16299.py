#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that adds numbers. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python add_numbers.py <filename>")
        sys.exit()
    
    filename = sys.argv[1]
    
    with open(filename, 'r') as f:
        numbers = f.read().splitlines()
    
    for number in numbers:
        number = int(number)
        
        if number > 0:
            print(number + 