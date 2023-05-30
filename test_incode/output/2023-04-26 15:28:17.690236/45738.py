#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints all ports or adds a list of numbers. """    
    ports = [int(p) for p in sys.argv[1:]]
    ports.sort()
    for port in ports:
        httpd = HTTPServer(('localhost', port), Handler)
        httpd.serve_forever()
    
