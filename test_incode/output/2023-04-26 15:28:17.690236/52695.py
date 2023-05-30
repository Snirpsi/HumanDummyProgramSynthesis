#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that iterates over a list of words and enumerates words. """    
    words = ['cat', 'dog', 'mouse']
    
    for index, word in enumerate(words):
        print('{}. {}'.format(index, word))
        
    print('Done!')
    
