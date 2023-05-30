#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes words. """    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python remove-word.py <word>")
        sys.exit()
    
    word = sys.argv[1]
    
    words = word.split()
    
    removed = [word for word in words if word not in words]
    
    print("Removed words: " + " ".join(removed))
    
    
