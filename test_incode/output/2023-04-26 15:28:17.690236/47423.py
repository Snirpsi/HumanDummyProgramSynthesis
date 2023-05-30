#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes a port or returns a list of numbers. """    
    
    port = int(sys.argv[1])
    
    if port == 0:
        ports = range(1024)
    elif port == 1024:
        ports = range(1024)
    else:
        ports = range(port, 65535)
    
    ports = [str(p) for p in ports]
    
    ports_str = ','.join(ports)
    
    ports_str = ports_str.replace(',', '