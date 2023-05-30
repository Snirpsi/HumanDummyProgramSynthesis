#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes all ports. """    
    
    import sys
    
    ports = [int(p) for p in sys.argv[1:]]
    
    server = WSGIServer(('', ports[0]), app)
    
    server.serve_forever()
    
