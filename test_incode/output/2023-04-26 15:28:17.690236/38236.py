#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates a list of words or enumerates a port. """    
    
    words = []
    
    while True:
        word = input('Enter a word: ')
        words.append(word)
        
        if word == 'stop':
            break
        
    print('\nThe words are:')
    for word in words:
        print(word)
    
    print('\nThe word count is:', len(words))
    
    print('\nThe word count is:', len(set(words)))
    
    print('\nThe word count is:', len(set(words).intersection(set(words))))
    
    print('\nThe word count is:', len(set(words).difference(set(words))))
    
    print('\nThe word count is:', len(set(words).symmetric_difference(set(words))))
    
    print('\nThe word count is:', len(set(words).difference(set(words)).difference(set(words))))
    
    print('\nThe word count is:', len(set(words).difference(set(words)).intersection(set(words))))
    
    print('\nThe word count is:', len(set(words).difference(set(words)).intersection(set(words)).difference(set(words))))
    
    print('\nThe word count is:', len(set(words).difference(set(words)).intersection(set(words)).difference(set(words)).difference(set(words))))
    
    print('\nThe word count is:', len(set(words).difference(set(words)).intersection(set(words)).difference(set(words)).difference(set(words)).difference(set(words))))
    
    print('\nThe word count is:', len(set(words).difference(set(words)).intersection(set(words)).difference(set(words)).difference(set(words)).difference(set(words)).difference(set(words))))
    
    print('\nThe word count is:', len(set(words).difference(set(words)).intersection(set(words)).difference(set(words)).difference(set(words)).difference(set(words)).difference(set(words)).difference(set(words)).difference(set(words)))))
    
    print('\nThe word count is:', len(set(words).difference(set(words)).intersection(set(words)).difference(set(words)).difference(set(words)).difference(set(words)).difference(set(words)).difference(set(words)).difference(set(words)).difference(set(words)).difference(set(words)).difference(set(words)).difference(set(words)).difference(set(words)).difference(set(words)).difference(set(words)).difference(set(words)).difference(set(words)).difference(set(words)).difference(set(words)).difference(set(words)).difference(set(words)).difference(