#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts numbers. """    
    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: %s <number>" % sys.argv[0])
        sys.exit(1)
    
    number = sys.argv[1]
    
    number = int(number)
    
    number = str(number)
    
    print(number)
    
