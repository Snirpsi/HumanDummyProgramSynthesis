#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a list of words. """    
    import sys
    import os
    
    words = []
    
    for arg in sys.argv[1:]:
        words.append(arg)
    
    words.sort()
    
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'words.txt')
    
    with open(path, 'w') as file:
        for word in words:
            file.write(word + '\n')
    
    print('\n'.join(words))
    
