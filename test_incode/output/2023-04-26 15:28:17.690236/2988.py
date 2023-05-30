#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates a list of words. """    
    words = ['cat', 'dog', 'mouse', 'lion', 'snake', 'monkey', 'bird']
    
    for index, word in enumerate(words):
        print('{0}. {1}'.format(index, word))
        
    print('Done.')
    
