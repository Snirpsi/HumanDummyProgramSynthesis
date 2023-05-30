#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes a list of words. """    
    import sys
    
    wordlist = sys.argv[1:]
    
    removed = remove_list(wordlist)
    
    if removed:
        print('\n'.join(removed))
    else:
        print('No words removed.')
    
    
