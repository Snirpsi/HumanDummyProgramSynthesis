#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates a list of words. """    
    words = ['word1', 'word2', 'word3']
    for idx, word in enumerate(words):
        print('%d\t%s' % (idx, word))
    
