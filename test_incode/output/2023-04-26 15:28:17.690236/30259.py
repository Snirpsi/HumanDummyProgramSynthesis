#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts user input or enumerates numbers. """    
    
    import sys
    
    if len(sys.argv) > 1:
        
        number = int(sys.argv[1])
        
        if number < 0 or number > 100:
            print("Invalid number")
            sys.exit(1)
        
        if number % 2 == 0:
            print("%d is even" % number)
        else:
            print("%d is odd" % number)
        
    else:
        print("Usage: %s [number]" % sys.argv[0])
        sys.exit(1)
        
