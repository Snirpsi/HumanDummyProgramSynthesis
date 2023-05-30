#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens words and adds a list of words. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s [words.txt]" % sys.argv[0])
        sys.exit()
    
    words = open(sys.argv[1]).read().splitlines()
    
    for word in words:
        
        word = word.strip()
        
        if word:
            
            print("%s\t%s" % (word, word))
            
        else:
            
            print("%s\t%s" % (word, "<empty>"))
            
