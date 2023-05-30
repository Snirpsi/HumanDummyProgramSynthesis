#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes words and removes words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        
        words = sys.argv[1:]
        
        remove_words(words)
        
    else:
        
        remove_words("word1 word2 word3 word4 word5")
        
