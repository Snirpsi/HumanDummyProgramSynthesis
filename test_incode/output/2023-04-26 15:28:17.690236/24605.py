#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that calculates a list of words. """    
    words = ['the', 'cat', 'jumped', 'over', 'the', 'lazy', 'dog']
    
    word_count = {}
    
    for word in words:
        if word not in word_count:
            word_count[word] = 1
        else:
            word_count[word] += 1
    
    print(word_count)
    
