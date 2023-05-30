#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that calculates a list of words. """    
    words = ['apple', 'banana', 'cherry']
    
    word_counts = Counter(words)
    
    for word, count in word_counts.items():
        print('{}: {}'.format(word, count))
    
