#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts words or opens all ports. """    
    
    import sys
    
    if len(sys.argv) == 1:
        print("Usage: %s [word|port]" % sys.argv[0])
        sys.exit()
    
    port = None
    word = None
    
    if len(sys.argv) == 2:
        word = sys.argv[1]
    elif len(sys.argv) == 3:
        word = sys.argv[2]
        
    if len(sys.argv) == 3:
        port = sys.argv[3]
    
    if port is not None:
        port = port.strip()
        
    if word is not None:
        word = word.strip()
    
    if word is not None and len(word) > 0:
        word = word.lower()
        
        ports = find_ports(word)
        
        for port in ports:
            print("%s -> %s" % (word, port))
            
    else:
        ports = find_ports(word)
        
        for port in ports:
            print("%s -> %s" % (word, port))
            
            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
