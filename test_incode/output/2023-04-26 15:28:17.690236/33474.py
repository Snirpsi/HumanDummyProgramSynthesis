#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens numbers or returns a list of numbers. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: python %s <numbers>' % sys.argv[0])
        sys.exit()
    
    numbers = sys.argv[1:]
    
    numbers_open = open