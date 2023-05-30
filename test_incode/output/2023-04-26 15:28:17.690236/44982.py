#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens a port and opens a port. """    
    
    httpd = HTTPServer(('', 80), Handler)
    httpd.serve_forever()
    
