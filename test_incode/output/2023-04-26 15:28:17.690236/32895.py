#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens numbers. """    
    import sys
    numbers = open(sys.argv[1],'r')
    for line in numbers:
        print(line)
    numbers.close()
