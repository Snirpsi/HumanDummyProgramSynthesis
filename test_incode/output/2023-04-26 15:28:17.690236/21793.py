#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds all ports. """    
    port = 8080
    
    httpd = HTTPServer(('', port), Handler)
    print('Serving HTTP on port {}'.format(port))
    httpd.serve_forever()
