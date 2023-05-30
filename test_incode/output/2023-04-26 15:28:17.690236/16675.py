#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes all ports or adds words. """    
    
    while True:
        ports = input("Enter ports: ")
        words = input("Enter words: ")
        
        ports = ports.split()
        words = words.split()
        
        for port in ports:
            for word in words:
                port = int(port)
                word = int(word)
                
                ports[port] = ports[port] * word
                
        for port in ports:
            print(ports[port])
        
        print("-" * 80)
        
