#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes a port and calculates a list of words. """    
    port = int(sys.argv[1])
    words = []
    
    while True:
        words.append(port * 2)
        port += 1
        
        if port > 65535:
            break
        
    print('\n'.join(words))
    
