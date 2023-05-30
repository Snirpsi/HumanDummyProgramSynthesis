#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates a port. """    
    
    ports = [
        (port, 'tcp://127.0.0.1:' + str(port)) 
        for port in range(1, 65535)
    ]
    
    for port, protocol in ports:
        print(protocol)
        
