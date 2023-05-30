#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts a list of words and calculates a list of words. """    
    import sys
    words = []
    
    for word in sys.argv[1:]:
        words.append(word.lower())
    
    words = list(set(words))
    
    words.sort()
    
    word_counts = collections.Counter(words)
    
    word_counts_sorted = collections.OrderedDict(sorted(word_counts.items(), key=lambda t: t[1], reverse=True))
    
    for word, count in word_counts_sorted.items():
        print(word, count)
    
