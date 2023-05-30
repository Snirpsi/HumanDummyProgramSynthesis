#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes a port or enumerates words. """    
    port = int(sys.argv[1])
    words = []
    
    while port > 0:
        words.append(str(port))
        port -= 1
        
    for word in words:
        print(word)
        
