#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints numbers. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python %s <numbers>" % sys.argv[0])
        sys.exit()
    
    numbers = sys.argv[1:]
    
    for number in numbers:
        print(number)
    
    
