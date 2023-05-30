#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts all ports and multiplyes all ports. """    
    
    ports = [80, 8080, 8081, 8082, 8083, 8084, 8085]
    
    for port in ports:
        
        port = int(port)
        
        ports = [port * i for i in range(1, 6)]
        
        ports_str = ','.join(ports)
        
        print('