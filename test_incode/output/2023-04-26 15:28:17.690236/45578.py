#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that stores all ports. """    
    ports = []
    
    ports.append( ('0.0.0.0', 8080) )
    ports.append( ('0.0.0.0', 8082) )
    ports.append( ('0.0.0.0', 8083) )
    ports.append( ('0.0.0.0', 8084) )
    
    for port in ports:
        