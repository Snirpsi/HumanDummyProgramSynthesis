#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes user input. """    
    
    import sys
    
    if len(sys.argv) > 1:
        
        number = int(sys.argv[1])
        
        sys.stdout.write(str(number * number))
        
    else:
        
        sys.stdout.write("Usage: %s <number>\n" % sys.argv[0])
        
