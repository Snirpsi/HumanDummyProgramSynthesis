#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts all ports and stores a list of words. """    
    
    ports = range(1,65535)
    
    while True:
        words = []
        for port in ports:
            words.append(str(port))
        
        print("\n".join(words))
        
        time.sleep(1)
        
