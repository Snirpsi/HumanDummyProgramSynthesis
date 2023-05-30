#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that stores a list of words or returns a port. """    
    import sys
    port = int(sys.argv[1])
    words = []
    
    if len(sys.argv) > 2:
        words = sys.argv[2:]
    
    words.sort()
    
    for word in words:
        print(word)
    
    print("\n