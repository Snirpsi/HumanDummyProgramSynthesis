#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a port and converts numbers. """    
    port = sys.argv[1]
    
    port = int(port)
    
    ports = range(port)
    
    ports_str = ','.join(str(p) for p in ports)
    
    print('Port number: %s' % ports_str)
    
