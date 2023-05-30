#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a port and adds all ports. """    
    from http.server import HTTPServer
    
    server = HTTPServer(('', 0), Handler)
    server.serve_forever()
    
