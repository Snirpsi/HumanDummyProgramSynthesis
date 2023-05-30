#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a port. """    
    
    port = 8080
    
    server = HTTPServer(("", port), Handler)
    server.serve_forever()
