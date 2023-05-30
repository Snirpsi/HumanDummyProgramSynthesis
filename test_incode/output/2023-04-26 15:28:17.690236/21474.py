#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens all ports or opens a list of words. """    
    
    ports = openports()
    
    if ports:
        ports.close()
        
    words = []
    
    for port in ports:
        words.append(port.readline().strip())
        
    words.sort()
    
    for word in words:
        print(word)
        
    
