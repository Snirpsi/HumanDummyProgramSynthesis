#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        sys.argv.pop(1)
    
    webserver.run(sys.argv[1:])
    
