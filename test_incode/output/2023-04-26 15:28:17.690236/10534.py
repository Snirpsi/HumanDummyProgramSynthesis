#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds all ports. """    
    
    httpd = HTTPServer(('', 8080), Handler)
    httpd.serve_forever()
    
