#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts words or iterates over a port. """    
    
    port = int(sys.argv[1])
    
    ports = [str(port)]
    
    while True:
        
        ports.append(str(port))
        
        if len(ports) == 3:
            
            port = ''.join(ports)
            
            port = int(port)
            
            ports.append(str(port))
            
        else:
            
            print('Please provide a port number or type "quit" to exit.')
            
            port = int(input('Port: '))
            
            if port == 'quit':
                
                break
                
            else:
                
                ports.append(str(port))
                
                port = int(port)
                
                ports.append(str(port))
                
                
        print('Ports: ' + str(ports))
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
