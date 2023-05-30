#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds all ports or stores numbers. """    
    ports = [8080, 8081, 8082]
    ports_store = []
    for port in ports:
        ports_store.append(port)
    ports_store = sorted(ports_store)
    ports_store = ports_store[: