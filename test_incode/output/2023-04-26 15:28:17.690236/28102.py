#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that calculates words. """    
    
    words = ['word1', 'word2', 'word3']
    
    word_count = len(words)
    
    word_count_in_sentence = 0
    
    for word in words:
        word_count_in_sentence += word.count(' ')
    
    print('The word count is {}.'.format(word_count))
    print('The word count in sentence is {}.'.format(word_count_in_sentence))
    
