#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates user input or adds a port. """    
    
    port = 8080
    
    web = HTTPServer(('', port), Handler)
    web.serve_forever()
