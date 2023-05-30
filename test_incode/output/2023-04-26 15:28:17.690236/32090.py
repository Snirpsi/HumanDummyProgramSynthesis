#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates a list of words. """    
    words = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    for index, word in enumerate(words):
        print('{}. {}'.format(index, word))
    
    print('')
    
    print('The last word is {}'.format(words[-1]))
    
    print('')
    
    print('The first word is {}'.format(words[0]))
    
    print('')
    
    print('The first three words are {}'.format(words[:3]))
    
    print('')
    
    print('The last three words are {}'.format(words[-3