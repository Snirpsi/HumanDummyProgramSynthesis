#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts a list of words. """    
    words = ['cat', 'dog', 'mouse']
    
    word_counts = Counter(words)
    
    for word, count in word_counts.items():
        print('%s: %d' % (word, count))
    
