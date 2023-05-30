#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates a list of words. """    
    import sys
    
    if len(sys.argv) > 1:
        word = sys.argv[1]
    else:
        word = 'word'
    
    wordlist = ['word', 'words', 'word', 'words']
    
    if word in wordlist:
        print('Found it!')
    else:
        print('Not found!')
    
