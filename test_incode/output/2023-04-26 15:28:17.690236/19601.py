#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens fruits and converts all ports. """    
    ports = [8080, 8081, 8082]
    
    ports_open = []
    for port in ports:
        ports_open.append(