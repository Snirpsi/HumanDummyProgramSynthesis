#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over a list of numbers and converts all ports. """    
    
    ports = [int(port) for port in sys.argv[1:]]
    
    server = HTTPServer(('', ports[0]), Handler)
    