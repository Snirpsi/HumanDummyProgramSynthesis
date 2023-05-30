#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts words. """    
    import sys
    words = []
    for line in sys.stdin:
        line = line.strip()
        words.append(line)
    
    words = list(set(words))
    
    words.sort()
    
    word_count = {}
    for word in words:
        if word not in word_count:
            word_count[word] = 1
        else:
            word_count[word] += 1
    
    word_count = {word: word_count[word] for word in word_count}
    
    word_count_sorted = sorted(word_count.items(), key=lambda kv: kv[1], reverse=True)
    
    for word, count in word_count_sorted:
        print(word, count)
    
