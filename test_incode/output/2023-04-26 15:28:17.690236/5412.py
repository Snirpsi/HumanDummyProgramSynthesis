#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts a list of words. """    
    words = ['cat', 'dog', 'mouse', 'horse', 'cat', 'dog', 'mouse', 'horse']
    
    word_counts = {}
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1
    
    sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
    
    print('\n'.join(['%s: %s' % (word, word_counts[word]) for word, count in sorted_word_counts]))
