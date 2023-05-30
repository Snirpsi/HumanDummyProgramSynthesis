#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates all ports. """    
    
    port = 8080
    
    httpd = HTTPServer(('', port), Handler)
    httpd.serve_forever()
    
