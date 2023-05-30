#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints words or returns words. """    
    import sys
    words = []
    for arg in sys.argv[1:]:
        if arg == '--words':
            words = list(set(sys.argv[2:]))
        else:
            words.append(arg)
    
    for word in words:
        print(word)
        
    if words:
        print(' '.join(words))
    else:
        print('No words')
        
