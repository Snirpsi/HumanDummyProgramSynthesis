#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a list of numbers and converts all ports. """    
    
    import sys
    
    ports = []
    
    for arg in sys.argv[1:]:
        ports.append(int(arg))
    
    for port in ports:
        
        server = Server()
        server.serve_forever()
    
