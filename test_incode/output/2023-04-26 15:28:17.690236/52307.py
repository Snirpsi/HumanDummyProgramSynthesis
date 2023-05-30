#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints words or removes all ports. """    
    import sys
    
    if len(sys.argv) > 1:
        word = sys.argv[1]
        
        if word.lower() in ['all', 'words', 'word', 'words']:
            word = 'words'
        else:
            word = 'word'
    
        print(word)
    else:
        print('No word given.')
        
