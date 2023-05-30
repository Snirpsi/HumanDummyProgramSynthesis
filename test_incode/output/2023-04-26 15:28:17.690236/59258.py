#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts user input or multiplyes words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        word = sys.argv[1]
        
        if word == 'quit':
            sys.exit(0)
        
        words = word.split()
        
        if len(words) == 1:
            word = '1'
            
        word = ''.join(words)
        
        print(word)
    else:
        print('Usage: python word