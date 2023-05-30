#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens words or adds words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        port = sys.argv[1]
    else:
        port = 8000
    
    webserver.serve(port)
    
