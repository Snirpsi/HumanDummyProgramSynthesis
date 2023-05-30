#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over all ports or removes words. """    
    
    ports = sys.argv[1:]
    
    for port in ports:
        
        port = int(port)
        
        words = port.split()
        
        for word in words:
            
            word = word.strip()
            
            if word != '':
                
                word = word.lower()
                
                if word in ports:
                    
                    ports.remove(word)
                    
                else:
                    
                    ports.add(word)
                    
            else:
                
                ports.add(word)
                
    print(ports)
    
