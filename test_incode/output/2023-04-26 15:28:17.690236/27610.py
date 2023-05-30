#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that adds words or enumerates a port. """    
    
    port = int(sys.argv[1])
    
    words = sys.argv[2:]
    
    words = [w.strip() for w in words]
    
    words = enumerate(words, start=port)
    
    for word, port in words:
        print(word, port)
    
