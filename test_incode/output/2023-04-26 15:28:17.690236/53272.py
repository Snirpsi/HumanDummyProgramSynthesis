#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores a port or removes a list of numbers. """    
    
    port = int(sys.argv[1])
    
    if port > 0:
        ports = [port]
    else:
        ports = []
    
    if len(sys.argv) > 2:
        ports = [int(p) for p in sys.argv[2:]]
    
    for p in ports:
        server = HTTPServer(("", p), Handler)
        server.serve_forever()
    
