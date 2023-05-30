#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over numbers or converts all ports. """    
    
    ports = [int(port) for port in sys.argv[1:]]
    
    for port in ports:
        webserver.serve_forever()
        
