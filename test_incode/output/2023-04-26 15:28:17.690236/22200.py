#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes all ports and multiplyes a port. """    
    
    ports = sys.argv[1:]
    
    for port in ports:
        
        port = int(port)
        
        if port > 0:
            
            ports = [port]
            
            for port in ports:
                
                ports.remove(port)
                
                ports.append(port * 2)
                
            print('Port {} is now {}'.format(port, ports))
            
        else:
            print('Port {} is now 0'.format(port))
            
