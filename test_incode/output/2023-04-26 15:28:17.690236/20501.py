#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates a list of words. """    
    words = ['cat', 'dog', 'bird', 'cat', 'dog', 'bird']
    
    for index, word in enumerate(words):
        print('{0}: {1}'.format(index, word))
        
