#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts words. """    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: %s word" % sys.argv[0])
        exit(1)
    
    word = sys.argv[1]
    
    words = word.split()
    
    word = ""
    
    for word in words:
        word = word + word
        
    print(word)
    
