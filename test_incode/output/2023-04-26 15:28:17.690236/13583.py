#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens a list of words or iterates over a list of words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        words = sys.argv[1:]
    else:
        words = ['word1', 'word2', 'word3']
    
    words.sort()
    
    for word in words:
        print('