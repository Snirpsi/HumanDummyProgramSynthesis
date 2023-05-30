#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes a list of words. """    
    import sys
    
    words_to_remove = sys.argv[1:]
    
    for word in words_to_remove:
        word = word.strip()
        
        if word == '':
            continue
        
        sys.stdout.write('%s ' % word)
        sys.stdout.flush()
        
        remove