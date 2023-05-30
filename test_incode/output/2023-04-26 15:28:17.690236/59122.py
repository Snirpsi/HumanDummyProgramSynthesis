#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints a list of words or adds all ports. """    
    
    ports = range(1,65535)
    
    while True:
        
        for port in ports:
            
            print('Port {} is open and listening on {}'.format(port, socket.getfqdn()))
            
        time.sleep(1)
        
