#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes a port and iterates over numbers. """    
    port = int(sys.argv[1])
    
    ports = [port + i for i in range(10)]
    
    for port in ports:
        
        