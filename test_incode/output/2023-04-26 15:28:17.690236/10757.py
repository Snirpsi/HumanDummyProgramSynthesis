#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes all ports. """    
    
    from http.server import HTTPServer
    
    httpd = HTTPServer(("", 0), Handler)
    
    httpd.serve_forever()
    
