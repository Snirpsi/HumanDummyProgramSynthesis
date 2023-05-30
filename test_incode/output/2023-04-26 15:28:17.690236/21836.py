#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over all ports. """    
    
    ports = range(8000, 8008)
    
    httpd = HTTPServer(('', 8000), Handler)
    httpd.serve_forever()
    
