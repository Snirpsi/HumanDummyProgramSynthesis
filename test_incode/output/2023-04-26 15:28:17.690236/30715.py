#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints numbers. """    
    import sys
    
    if len(sys.argv) > 1:
        number = int(sys.argv[1])
        
        for i in range(number):
            print(i)
    else:
        print("Usage: python3 