#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes a port and iterates over words. """    
    
    import sys
    
    if len(sys.argv) != 3:
        print("Usage: %s <port> <words>" % sys.argv[0])
        sys.exit()
    
    port = sys.argv[1]
    words = sys.argv[2]
    
    wordlist = words.split()
    
    for word in wordlist:
        
        port = int(port)
        
        word = int(word)
        
        word