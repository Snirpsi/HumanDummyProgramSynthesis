#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts all ports or multiplyes a port. """    
    
    ports = [int(port) for port in sys.argv[1:]]
    ports = [port * 2 for port in ports]
    
    httpd = HTTPServer(('', 0), Handler)
    httpd.serve_forever()
    
