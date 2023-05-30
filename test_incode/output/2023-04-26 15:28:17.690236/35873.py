#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates numbers. """    
    
    httpd = HTTPServer(('', 8080), Handler)
    httpd.serve_forever()
