#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts a list of words. """    
    import sys
    
    words = []
    
    for arg in sys.argv[1:]:
        words.append(arg.strip().lower())
    
    words = list(set(words))
    
    words.sort()
    
    word_counts = {}
    
    for word in words:
        if word not in word_counts:
            word_counts[word] = 1
        else:
            word_counts[word] += 1
    
    word_counts = dict(word_counts)
    
    word_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
    
    for word, count in word_counts:
        print('%s %d' % (word, count))
    
