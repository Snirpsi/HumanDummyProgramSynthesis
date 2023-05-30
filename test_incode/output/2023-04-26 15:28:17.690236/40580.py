#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts numbers. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python3 convert.py <number>")
        sys.exit()
    
    number = sys.argv[1]
    
    number = int(number)
    
    if number < 0:
        print("Error: negative numbers not allowed")
        sys.exit()
    
    number = str(number)
    
    number = number.replace(",", "")
    
    number = number.replace("(", "")
    
    number = number.replace(")", "")
    
    number = number.replace("'", "")
    
    number = number.replace("