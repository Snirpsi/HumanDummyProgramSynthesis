#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over a list of numbers. """    
    
    import os
    import sys
    
    port = int(sys.argv[1])
    
    os.environ['PORT'] = str(port)
    
    webserver = WSGIServer(('', port), Handler)
    webserver.serve_forever()
    
