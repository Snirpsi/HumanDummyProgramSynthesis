#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds a list of words or prints words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        words = sys.argv[1:]
    else:
        words = ['word1', 'word2', 'word3']
    
    words = [word.upper() for word in words]
    
    sys.stdout.write('\n'.join(words))
    
