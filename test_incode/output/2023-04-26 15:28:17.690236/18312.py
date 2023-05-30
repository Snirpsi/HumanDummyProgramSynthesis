#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores a port. """    
    port = int(sys.argv[1])
    httpd = HTTPServer(('localhost', port), Handler)
    httpd.serve_forever()
