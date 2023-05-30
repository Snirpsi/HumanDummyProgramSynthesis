#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints a list of numbers or converts numbers. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python numberlist.py <numbers>")
        sys.exit()
    
    numbers = sys.argv[1:]
    
    for number in numbers:
        print(number)
        
