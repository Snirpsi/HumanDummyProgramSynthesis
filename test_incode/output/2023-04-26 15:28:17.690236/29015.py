#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds a port and stores a list of words. """    
    
    port = 0
    words = []
    
    while True:
        port = port + 1
        
        if port > 65535:
            port = port - 1
        
        words.append(str(port))
        
        print("Port " + str(port) + ": " + " ".join(words))
        
        time.sleep(1)
        
