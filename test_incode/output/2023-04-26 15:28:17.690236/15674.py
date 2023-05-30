#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores a list of words and enumerates words. """    
    words = []
    
    while True:
        word = input('Enter a word: ')
        
        if word == '':
            break
        
        words.append(word)
        
    print('\n'.join('%s => %s' % (word, index) for index, word in enumerate(words)))
    
