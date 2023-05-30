#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds a port or adds a list of numbers. """    
    
    port = int(sys.argv[1])
    
    if port > 0:
        server = HTTPServer(("", port), Handler)
        server.serve_forever()
    else:
        ports = sys.argv[2:]
        
        for port in ports:
            server = HTTPServer(("", port), Handler)
            server.serve_forever()
            
