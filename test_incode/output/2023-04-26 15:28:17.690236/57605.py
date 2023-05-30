#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts all ports. """    
    port = 80
    
    httpd = HTTPServer(('', port), Handler)
    httpd.serve_forever()
