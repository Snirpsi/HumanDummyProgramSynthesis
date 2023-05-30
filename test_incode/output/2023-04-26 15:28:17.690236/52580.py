#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes numbers or enumerates all ports. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python remove_ports.py <ports>")
        sys.exit()
    
    ports = sys.argv[1:]
    
    for port in ports:
        
        if port.isdigit():
            
            port = int(port)
            
            if port < 1 or port > 65535:
                print("Port number must be between 1 and 65535")
                sys.exit(1)
                
        else:
            
            ports = port.split(',')
            
            for port in ports:
                
                if port.isdigit():
                    
                    port = int(port)
                    
                    if port < 1 or port > 65535:
                        print("Port number must be between 1 and 65535")
                        sys.exit(1)
                        
                else:
                    
                    ports = port.split(',')
                    
                    for port in ports:
                        
                        if port.isdigit():
                            
                            port = int(port)
                            
                            if port < 1 or port > 65535:
                                print("Port number must be between 1 and 65535")
                                sys.exit(1)
                            
                        else:
                            
                            ports = port.split(',')
                            
                            for port in ports:
                                
                                if port.isdigit():
                                    
                                    port = int(port)
                                    
                                    if port < 1 or port > 65535:
                                        print("Port number must be between 1 and 65535")
                                        sys.exit(1)
                                    
