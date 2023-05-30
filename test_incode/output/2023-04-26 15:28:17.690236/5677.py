#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints words and stores all ports. """    
    
    ports = []
    
    ports.append(8080)
    ports.append(8000)
    ports.append(8081)
    ports.append(8082)
    ports.append(8083)
    
    ports_str = []
    for port in ports:
        ports_str.append("{}:{}".format(port, 