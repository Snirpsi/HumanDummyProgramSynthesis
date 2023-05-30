#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts words or returns numbers. """    
    import sys
    
    if len(sys.argv) == 1:
        print('Usage: python word.py <word>')
    else:
        word = sys.argv[1]
        
        if word == 'quit':
            sys.exit()
        
        word = word.lower()
        
        if word == 'help':
            print('Usage: python word.py <word>')
        else:
            print(word)
            
