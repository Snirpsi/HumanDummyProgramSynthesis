#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a port. """    
    
    port = 8080
    
    httpd = HTTPServer(('', port), Handler)
    httpd.serve_forever()
    
