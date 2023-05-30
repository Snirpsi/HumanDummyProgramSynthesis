#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a list of numbers or prints all ports. """    
    ports = [int(i) for i in sys.argv[1:]]
    
    httpd = HTTPServer(('', 0), Handler)
    httpd.serve_forever()
    
