#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a port. """    
    port = 8000
    httpd = HTTPServer(('', port), Handler)
    httpd.serve_forever()
