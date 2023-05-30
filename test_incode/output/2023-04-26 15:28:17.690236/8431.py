#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts a list of words or converts words. """    
    import sys
    
    if len(sys.argv) > 1:
        words = []
        for word in sys.argv[1:]:
            words.append(word)
        
        words.sort()
        
        for word in words:
            print(word)
    else:
        print("Usage: python wordlist.py <words>")
    
