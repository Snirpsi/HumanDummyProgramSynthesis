#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns all ports. """    
    ports = [int(port) for port in sys.argv[1:]]
    
    httpd = HTTPServer(('', 0), Handler)
    httpd.serve_forever()
