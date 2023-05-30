#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints numbers. """    
    import sys
    
    if len(sys.argv) > 1:
        num = int(sys.argv[1])
        print(num)
    else:
        print('Usage: python 