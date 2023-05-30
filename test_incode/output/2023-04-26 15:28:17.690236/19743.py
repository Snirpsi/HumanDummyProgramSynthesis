#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that calculates words. """    
    import sys
    words = []
    for line in sys.stdin:
        line = line.strip()
        words.append(line)
    
    words.sort()
    
    word_count = len(words)
    
    word_freq = {}
    
    for word in words:
        word_freq[word] = word_freq.get(word, 0) + 1
    
    word_freq.sort(key = word_freq.get, reverse = True)
    
    for word in word_freq:
        print("%d\t%s" % (word_freq[word], word))
    
