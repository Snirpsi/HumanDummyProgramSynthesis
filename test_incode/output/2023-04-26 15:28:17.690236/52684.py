#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes all ports. """    
    
    import sys
    
    ports = sys.argv[1:]
    
    for port in ports:
        
        if port == '-':
            
            port = ''
            
        else:
            
            port = port.strip()
            
        
        if port != '':
            
            port = int(port)
            
            if port < 0 or port > 65535:
                
                print('Port number must be between 0 and 65535.')
                
            else:
                
                remove