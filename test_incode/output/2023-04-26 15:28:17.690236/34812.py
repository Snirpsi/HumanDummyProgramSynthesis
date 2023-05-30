#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that prints a list of words. """    
    words = ['cat', 'dog', 'mouse', 'bird', 'cat', 'dog', 'mouse', 'bird']
    
    word_counts = collections.Counter(words)
    
    print('The words and their counts are:')
    for word, count in word_counts.items():
        print('{}: {}'.format(word, count))
        
