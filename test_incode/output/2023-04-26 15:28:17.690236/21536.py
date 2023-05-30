#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over all ports. """    
    
    import os
    import sys
    
    port = int(sys.argv[1])
    
    os.environ['PORT'] = str(port)
    
    web = WebServer()
    web.serve_forever()
    
