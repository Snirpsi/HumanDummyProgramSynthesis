#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that calculates a list of words. """    
    words = ['word1', 'word2', 'word3', 'word4', 'word5']
    
    word_counts = Counter(words)
    
    word_counts_sorted = sorted(word_counts.items(), key=lambda x: x[1])
    
    print(word_counts_sorted)
    
