#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens all ports. """    
    
    httpd = HTTPServer(('', 0), Handler)
    httpd.serve_forever()
    
