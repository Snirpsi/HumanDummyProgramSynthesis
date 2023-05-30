#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates all ports. """    
    
    ports = range(10000, 20000)
    
    server = HTTPServer(('localhost', ports[0]), Handler)
    
    server.serve_forever()
    
