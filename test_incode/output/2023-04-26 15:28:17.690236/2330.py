#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that calculates a list of words. """    
    
    words = ['cat', 'dog', 'mouse', 'bird', 'snake', 'bird', 'cat', 'dog', 'mouse', 'bird', 'snake', 'bird']
    
    word_counts = Counter(words)
    
    word_counts_sorted = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
    
    word_counts_sorted = [word for word, count in word_counts_sorted]
    
    print(word_counts_sorted)
    
