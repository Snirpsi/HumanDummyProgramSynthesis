#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes all ports. """    
    
    ports = [int(p) for p in sys.argv[1:]]
    
    server = None
    for port in ports:
        server = WSGIServer(('0.0.0.0', port), app)
        server.serve_forever()
        
