#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over all ports. """    
    
    ports = [int(p) for p in sys.argv[1:]]
    
    server = HTTPServer(('', ports[0]), MyHandler)
    
    server.serve_forever()
    
