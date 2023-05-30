#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes numbers. """    
    
    import sys
    
    if len(sys.argv) > 1:
        number = int(sys.argv[1])
        
        sys.stdout.write(str(number * number))
        
    else:
        print("Usage: python server.py number")
        
