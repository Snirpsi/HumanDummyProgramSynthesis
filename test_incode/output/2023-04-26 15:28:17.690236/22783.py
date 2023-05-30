#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over words and calculates a list of words. """    
    import sys
    words = []
    for line in sys.stdin:
        line = line.strip()
        if line == '':
            continue
        words.append(line)
    
    words.sort()
    
    word_counts = {}
    for word in words:
        if word not in word_counts:
            word_counts[word] = 1
        else:
            word_counts[word] += 1
    
    word_counts = sorted(word_counts.items(), key=lambda kv: kv[1], reverse=True)
    
    for word, count in word_counts:
        print(word, count)
    
