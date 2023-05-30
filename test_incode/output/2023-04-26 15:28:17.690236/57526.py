#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens all ports. """    
    
    webserver = HTTPServer(('', 8080), Handler)
    webserver.serve_forever()
    
