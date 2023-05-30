#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds all ports. """    
    
    ports = range(8000, 8009)
    
    httpd = HTTPServer(("", 0), Handler)
    httpd.serve_forever()
    
