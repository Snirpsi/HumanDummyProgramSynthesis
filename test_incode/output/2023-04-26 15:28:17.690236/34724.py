#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes a port or returns a list of numbers. """    
    port = int(sys.argv[1])
    
    ports = [port for port in range(1024)]
    
    ports.remove(port)
    
    print('\n'.join(map(str, ports)))
    
