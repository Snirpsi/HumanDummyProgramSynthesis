#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts a list of words. """    
    import sys
    
    words = []
    for arg in sys.argv[1:]:
        words.append(arg)
    
    words.sort()
    
    i = 0
    
    while(i < len(words)):
        word = words[i]
        
        if(i < len(words) - 1):
            word = word + " "
        
        sys.stdout.write(word)
        
        i = i + 1
        
        sys.stdout.write("\n")
    
