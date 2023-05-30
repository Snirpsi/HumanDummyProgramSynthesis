#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that prints words or adds a list of words. """    
    import sys
    words = []
    for arg in sys.argv[1:]:
        words.append(arg)
    
    if len(words) == 0:
        print('No words given.')
    else:
        print('Words:')
        for word in words:
            print(word)
    
