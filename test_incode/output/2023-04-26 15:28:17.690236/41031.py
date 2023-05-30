#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints all ports. """    
    ports = []
    
    ports.append(8080)
    ports.append(8000)
    ports.append(9000)
    ports.append(10000)
    
    for port in ports:
        print('Starting webserver on port ' + str(port))
        
        webserver.run(port=port)
        
