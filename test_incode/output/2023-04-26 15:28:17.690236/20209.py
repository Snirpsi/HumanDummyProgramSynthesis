#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates a port and iterates over words. """    
    
    words = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    port = 1
    
    while True:
        port = port + 1
        
        print('Port {}: {}'.format(port, words[port]))
        
        if port == len(words):
            break
        
        time.sleep(1)
        
    print('Done.')
    
