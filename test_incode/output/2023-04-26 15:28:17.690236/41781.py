#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes fruits. """    
    
    httpd = HTTPServer(('localhost', 8000), Handler)
    httpd.serve_forever()
    
