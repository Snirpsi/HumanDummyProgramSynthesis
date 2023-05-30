#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates a list of words. """    
    words = ['cat', 'dog', 'mouse', 'elephant', 'bird', 'cat', 'dog', 'mouse', 'elephant', 'bird']
    
    for index, word in enumerate(words):
        print('{}: {}'.format(index, word))
    
    print('\n')
    
    print('