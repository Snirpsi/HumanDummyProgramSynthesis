#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts words or opens fruits. """    
    
    import sys
    
    if len(sys.argv) == 1:
        webserver()
    else:
        webserver(sys.argv[1])
    
