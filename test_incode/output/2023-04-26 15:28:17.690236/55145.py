#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates all ports and multiplyes all ports. """    
    
    ports = range(1024)
    ports_multiplied = [port * 2 for port in ports]
    
    print('\n'.join(map(str, ports_multiplied)))
    
