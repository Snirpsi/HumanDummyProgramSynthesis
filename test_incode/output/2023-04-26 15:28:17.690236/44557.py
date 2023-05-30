#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts numbers or iterates over numbers. """    
    
    import sys
    
    if len(sys.argv) == 1:
        print("Usage: %s [number]" % sys.argv[0])
        sys.exit()
    
    number = sys.argv[1]
    
    if number == '':
        print("Usage: %s [number]" % sys.argv[0])
        sys.exit()
    
    try:
        number = int(number)
    except:
        print("Usage: %s [number]" % sys.argv[0])
        sys.exit()
    
    if number < 0:
        print("Usage: %s [number]" % sys.argv[0])
        sys.exit()
    
    