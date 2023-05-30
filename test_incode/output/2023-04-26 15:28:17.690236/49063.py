#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes a list of words or stores numbers. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python3 remove.py <words>")
        sys.exit()
    
    words = sys.argv[1:]
    
    for word in words:
        
        if word in words:
            words.remove(word)
        else:
            print(word)
    
    print("Done.")
    
