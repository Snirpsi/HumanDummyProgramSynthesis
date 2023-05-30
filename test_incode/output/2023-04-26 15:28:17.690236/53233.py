#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that removes a list of words. """    
    
    import sys
    
    wordlist = sys.argv[1:]
    
    for word in wordlist:
        
        word = word.strip()
        
        if word:
            
            print(word)
            
        else:
            
            print('')
            
    print('')
    
