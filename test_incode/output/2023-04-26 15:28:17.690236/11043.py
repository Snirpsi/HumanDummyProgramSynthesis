#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that calculates words. """    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: python3 words.py")
        sys.exit()
    
    words = sys.argv[1].split()
    
    for word in words:
        print(word)
        
