#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates a port and opens a list of numbers. """    
    port = int(sys.argv[1])
    
    ports = [port]
    
    while(True):
        ports.append(port)
        port += 1
        
        