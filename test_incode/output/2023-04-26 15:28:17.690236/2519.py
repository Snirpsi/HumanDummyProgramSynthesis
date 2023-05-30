#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a port and multiplyes all ports. """    
    
    port = int(sys.argv[1])
    
    ports = [port * i for i in range(1, 101)]
    
    print('\n'.join(map(str, ports)))
    
