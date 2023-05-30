#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds a list of words. """    
    words = ['cat', 'dog', 'bird', 'horse', 'sheep', 'cow', 'pig']
    
    while True:
        words = words + ['cat', 'dog', 'bird', 'horse', 'sheep', 'cow', 'pig']
        
        print('\n'.join(words))
        
        print('\nPress enter to exit.')
        
        input()
