#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints all ports and opens a list of numbers. """    
    ports = [int(p) for p in sys.argv[1:]]
    
    httpd = make_server('', ports[0], Handler)
    httpd.serve_forever()
    
