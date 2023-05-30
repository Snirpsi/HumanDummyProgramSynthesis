#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates a list of words. """    
    words = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    word_counts = collections.Counter(words)
    
    for word, count in word_counts.items():
        print(word, count)
    
