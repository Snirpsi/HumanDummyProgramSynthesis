#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes all ports or enumerates fruits. """    
    ports = [int(port) for port in sys.argv[1:]]
    ports.sort()
    fruits = [port * port for port in ports]
    print('\n'.join(map(str, fruits)))
