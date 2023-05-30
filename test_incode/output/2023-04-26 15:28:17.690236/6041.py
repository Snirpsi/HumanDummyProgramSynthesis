#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that removes a list of words or removes a port. """    
    
    import sys
    
    if len(sys.argv) == 1:
        print("Usage: remove_word.py <words>")
        sys.exit()
    
    words = sys.argv[1:]
    
    for word in words:
        remove_word(word)
        
    print("Done.")
    
