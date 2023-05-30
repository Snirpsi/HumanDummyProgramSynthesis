#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates all ports. """    
    ports = []
    
    server = HTTPServer(("", 0), Handler)
    server.serve_forever()
    
