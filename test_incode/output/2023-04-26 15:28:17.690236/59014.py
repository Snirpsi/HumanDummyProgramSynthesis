#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds all ports and converts words. """    
    ports = [8080, 8081, 8082, 8083, 8084, 8085]
    
    ports_str = [str(p) for p in ports]
    
    ports_str = ','.join(ports_str)
    
    ports_str = ports_str.replace(',', '