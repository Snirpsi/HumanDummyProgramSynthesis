#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that calculates a port or calculates a list of words. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <port>" % sys.argv[0])
        sys.exit()
    
    port = sys.argv[1]
    
    words = []
    
    for word in port.split():
        words.append(word)
    
    print("\n".join(words))
    
