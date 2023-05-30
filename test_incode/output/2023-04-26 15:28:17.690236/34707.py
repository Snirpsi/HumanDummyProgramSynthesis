#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that stores words. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python store.py <filename>")
        sys.exit()
    
    filename = sys.argv[1]
    
    words = open(filename).read().split()
    
    store = dict()
    
    for word in words:
        if word not in store:
            store[word] = 1
        else:
            store[word] += 1
    
    for word in store:
        print(word, store[word])
    
