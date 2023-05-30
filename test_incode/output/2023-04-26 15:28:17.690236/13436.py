#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a list of words. """    
    
    import os
    
    words = []
    
    for root, dirs, files in os.walk('wordlist'):
        for filename in files:
            words.append(os.path.join(root, filename))
    
    print('\n'.join(words))
    
