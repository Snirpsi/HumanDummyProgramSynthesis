#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts numbers. """    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s number" % sys.argv[0])
        sys.exit()
    
    number = sys.argv[1]
    
    try:
        number = int(number)
    except ValueError:
        print("Usage: %s number" % sys.argv[0])
        sys.exit()
    
    number = str(number)
    
    number = number.replace('.', '')
    number = number.replace('-', '')
    number = number.replace('/', '')
    
    print(number)
    
