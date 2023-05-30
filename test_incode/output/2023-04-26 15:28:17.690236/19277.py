#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds all ports. """    
    
    port = sys.argv[1]
    
    httpd = HTTPServer(('', port), Handler)
    httpd.serve_forever()
    
