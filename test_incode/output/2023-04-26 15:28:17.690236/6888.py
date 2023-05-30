#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates a list of words. """    
    words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    
    for index, word in enumerate(words):
        print('%d\t%s' % (index, word))
    
    print('\nPress Ctrl-C to exit')
    
    