#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that calculates words. """    
    
    words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    
    word_count = {}
    
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    
    for word in word_count:
        print('%s: %d' % (word, word_count[word]))
    
