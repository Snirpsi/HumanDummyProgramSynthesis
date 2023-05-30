#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes a list of words and enumerates user input. """    
    
    words = ['hello', 'world', 'how', 'are', 'you', 'today']
    
    words_enum = enumerate(words)
    
    for index, word in words_enum:
        print('{}. {}'.format(index+1, word))
    
