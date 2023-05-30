#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts words. """    
    
    import sys
    
    if len(sys.argv) != 2:
        print('Usage: %s words.txt' % sys.argv[0])
        sys.exit(1)
    
    words = []
    with open(sys.argv[1]) as f:
        for line in f:
            words.append(line.strip())
    
    words = list(set(words))
    
    words.sort()
    
    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    
    word_counts = dict(word_counts.items())
    word_counts = dict(sorted(word_counts.items(), key=lambda x: x[1], reverse=True))
    
    word_counts_sorted = []
    for word, count in word_counts.items():
        word_counts_sorted.append([word, count])
    
    word_counts_sorted.sort(key=lambda x: x[1], reverse=True)
    
    for word, count in word_counts_sorted:
        print(word, count)
    
