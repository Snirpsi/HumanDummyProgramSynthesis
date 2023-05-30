#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes words and enumerates all ports. """    
    import sys
    
    ports = []
    
    for arg in sys.argv[1:]:
        ports.append(int(arg))
    
    ports.sort()
    
    for port in ports:
        
        word = sys.argv[1]
        
        if word in ports:
            
            ports.remove(word)
            
            print(port)
            
        else:
            print("Port %s is not in %s" % (word, ports))
    
