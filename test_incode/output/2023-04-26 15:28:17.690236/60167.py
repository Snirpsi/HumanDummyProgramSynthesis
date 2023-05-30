#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns a list of words and stores a list of words. """    
    words = []
    
    while True:
        words.append(input('Enter a word: '))
        
        if words[-1] == 'q':
            break
        
    print('The words are:')
    for word in words:
        print(word)
    
    print('\nThe word counts are:')
    word_counts = collections.Counter(words)
    for word, count in word_counts.items():
        print('{}: {}'.format(word, count))
    
    print('\nThe most common words are:')
    word_counts = collections.Counter(words).most_common()
    for word, count in word_counts:
        print('{}: {}'.format(word, count))
    
    print('\nThe least common words are:')
    word_counts = collections.Counter(words).