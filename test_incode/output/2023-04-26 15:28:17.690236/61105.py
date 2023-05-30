#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes a port or iterates over words. """    
    
    import sys
    
    ports = []
    
    if len(sys.argv) > 1:
        ports = sys.argv[1:]
    
    for port in ports:
        
        port = int(port)
        
        if port in ports:
            
            ports.remove(port)
            
        else:
            
            words = port.split()
            
            for word in words:
                
                word = word.strip()
                
                if word:
                    
                    ports.append(word)
                    
                else:
                    
                    ports.append("")
                    
    print("\n".join(ports))
    
