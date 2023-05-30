#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that stores a list of words. """    
    words = ['cat', 'dog', 'bird', 'lion', 'monkey']
    
    word_counts = Counter(words)
    
    print('The word counts are:')
    for word, count in word_counts.items():
        print('%s: %d' % (word, count))
    
    print('The most common words are:')
    for word, count in word_counts.most_common():
        print('%s: %d' % (word, count))
    
    print('The least common words are:')
    for word, count in word_counts.most_common():
        if count < 5:
            print('%s: %d' % (word, count))
    
    print('The most common words are:')
    for word, count in word_counts.most_common():
        if count > 5:
            print('%s: %d' % (word, count))
    
    print('The least common words are:')
    for word, count in word_counts.most_common():
        if count < 5:
            print('%s: %d' % (word, count))
    
    print('The most common words are:')
    for word, count in word_counts.most_common():
        if count > 5:
            print('%s: %d' % (word, count))
    
    print('The least common words are:')
    for word, count in word_counts.most_common():
        if count < 5:
            print('%s: %d' % (word, count))
    
    print('The most common words are:')
    for word, count in word_counts.most_common():
        if count > 5:
            print('%s: %d' % (word, count))
    
    print('The least common words are:')
    for word, count in word_counts.most_common():
        if count < 5:
            print('%s: %d' % (word, count))
    
    print('The most common words are:')
    for word, count in word_counts.most_common():
        if count > 5:
            print('%s: %d' % (word, count))
    
    print('The least common words are:')
    for word, count in word_counts.most_common():
        if count < 5:
            print('%s: %d' % (word, count))
    
    print('The most common words are:')
    for word, count in word_counts.most_common():
        if count > 5:
            print('%s: %d' % (word, count))
    
    print('The least common words are:')
    for word, count in word_counts.most_common():
        if count < 5:
            print('%s: %d' % (word, count))
    
    print('The most common words are:')
    for word, count in word_counts.most_common():
        if count > 5:
            print('%s: %d' % (word, count))
    
    print('The least common words are:')
    for word, count in word_counts.most_common():
        if count < 5:
            print('%s: %d' % (word, count))
    
    print('The most common words are:')
    for word, count in word_counts.most_common():
        if count > 5:
            print('%s: %d' % (word, count))
    
    print('The 