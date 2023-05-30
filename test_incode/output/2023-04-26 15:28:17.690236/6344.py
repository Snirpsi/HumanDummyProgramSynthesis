#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds a port. """    
    port = int(sys.argv[1])
    httpd = HTTPServer(('', port), Handler)
    print('Serving on port {}'.format(port))
    httpd.serve_forever()
