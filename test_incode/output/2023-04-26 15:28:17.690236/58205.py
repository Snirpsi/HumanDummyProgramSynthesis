#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates a list of words. """    
    words = ['hello', 'world', 'python', 'is', 'fun']
    for index, word in enumerate(words):
        print('{}. {}'.format(index, word))
