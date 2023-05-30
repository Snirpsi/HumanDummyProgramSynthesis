#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds numbers and converts all ports. """    
    
    port = 8080
    
    server = HTTPServer(('', port), Handler)
    
    server.serve_forever()
    
