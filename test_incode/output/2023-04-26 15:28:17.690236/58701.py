#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts numbers. """    
    import sys
    if len(sys.argv) < 2:
        print("Usage: python converter.py <number>")
        sys.exit()
    number = sys.argv[1]
    number = int(number)
    number = str(number)
    print(number)
    
