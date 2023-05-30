#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates user input. """    
    
    import sys
    
    if len(sys.argv) > 1:
        
        sys.stdout.write(sys.argv[1])
        
    else:
        
        sys.stdout.write("Usage: %s <port>\n" % sys.argv[0])
        
    sys.exit()
    
