#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that iterates over words and converts a port. """    
    
    import sys
    
    port = int(sys.argv[1])
    
    for word in sys.argv[2:]:
        word = word.strip()
        
        if word:
            print(word, end=' ')
            
            if word[0].isdigit():
                word = word[1:]
                
                print(word, end=' ')
                
                port = int(word)
                
                if port > 0:
                    