#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes words and iterates over all ports. """    
    
    ports = range(0,65535)
    
    while True:
        word = ''.join(str(x) for x in ports)
        
        print(word)
        
        ports *= 2
        
        time.sleep(1)
        
