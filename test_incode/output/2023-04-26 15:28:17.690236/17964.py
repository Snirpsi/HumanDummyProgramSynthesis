#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that adds words or adds words. """    
    
    import sys
    
    words = sys.argv[1:]
    
    for word in words:
        
        if word == '-h':
            
            print('Usage: python add_word.py word1 word2 word3 ...')
            
            sys.exit(0)
        
        else:
            
            print(add_word(word))
            
