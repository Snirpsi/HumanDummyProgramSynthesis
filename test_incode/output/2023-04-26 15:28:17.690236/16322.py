#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens a list of words. """    
    
    words = ['cat', 'dog', 'bird', 'mouse', 'cat', 'dog', 'bird']
    
    while True:
        
        print('\n'.join('{} - {}'.format(word, 