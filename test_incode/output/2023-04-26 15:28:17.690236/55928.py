#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes fruits. """    
    
    import os
    import sys
    
    port = int(sys.argv[1])
    
    os.environ['SERVER_PORT'] = str(port)
    
    web