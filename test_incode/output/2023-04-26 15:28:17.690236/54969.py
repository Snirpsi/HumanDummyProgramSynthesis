#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens all ports or stores a list of words. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <port>" % sys.argv[0])
        sys.exit()
    
    port = int(sys.argv[1])
    
    words = []
    
    with open('/etc/wordlist', 'r') as f:
        for line in f:
            words.append(line.strip())
    
    for word in words:
        
        if port == int(word):
            print(word)
    
