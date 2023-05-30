#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that stores numbers or adds words. """    
    
    import sys
    
    if len(sys.argv) == 1:
        print("Usage: python store.py <word>", file=sys.stderr)
        sys.exit()
    
    word = sys.argv[1]
    
    store = Store()
    store.add(word)
    
    print("Stored 