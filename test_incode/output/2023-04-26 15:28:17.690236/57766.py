#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a list of words and removes a list of words. """    
    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: %s words.txt" % sys.argv[0])
        sys.exit()
    
    words = [line.strip() for line in open(sys.argv[1])]
    
    words = set(words)
    
    for word in words:
        if word in words:
            words.remove(word)
    
    for word in words:
        print(word)
    
