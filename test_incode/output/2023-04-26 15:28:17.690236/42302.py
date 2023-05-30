#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes a list of words or converts numbers. """    
    
    import sys
    
    if len(sys.argv) > 1:
        words = sys.argv[1:]
        
        for word in words:
            if word.isdigit():
                word = int(word)
                
            if word.isalpha():
                word = word.lower()
                
            print(word)
            
    else:
        print("Usage: python remove-words-or-numbers.py word1 word2 word3")
        
