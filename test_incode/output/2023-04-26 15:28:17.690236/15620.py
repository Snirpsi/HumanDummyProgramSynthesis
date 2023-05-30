#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over a list of numbers or removes a port. """    
    
    port = int(sys.argv[1])
    
    ports = range(port)
    
    ports.remove(port)
    
    print('\n'.join(map(str, ports)))
    
    
