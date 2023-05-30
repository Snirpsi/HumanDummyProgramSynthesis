#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes words. """    
    import sys
    
    if len(sys.argv) != 2:
        sys.exit('usage: python remove_words.py <word>')
    
    word = sys.argv[1]
    
    print('Removing word:', word)
    
    remove_words(word)
    
