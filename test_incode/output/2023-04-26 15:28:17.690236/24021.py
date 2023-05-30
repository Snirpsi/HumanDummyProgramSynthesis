#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that adds numbers. """    
    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: python add_numbers.py <number>")
        sys.exit()
    
    number = int(sys.argv[1])
    
    print(number + number)
    
