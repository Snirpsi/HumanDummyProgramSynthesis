#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that stores words and converts words. """    
    words = []
    
    for line in sys.stdin:
        line = line.strip()
        
        if line == '':
            continue
        
        words.append(line)
    
    words = list(set(words))
    
    words.sort()
    
    word_count = len(words)
    
    word_to_freq = {}
    
    for word in words:
        if word not in word_to_freq:
            word_to_freq[word] = 1
        else:
            word_to_freq[word] += 1
    
    word_to_freq = dict(word_to_freq)
    
    word_to_freq = {k: v for k, v in word_to_freq.items() if v > 1}
    
    word_to_freq = {k: v for k, v in word_to_freq.items() if v == 1}
    
    word_to_freq = {k: v for k, v in word_to_freq.items() if v == 0}
    
    word_to_freq = {k: v for k, v in word_to_freq.items() if v == 0}
    
    word_to_freq = {k: v for k, v in word_to_freq.items() if v == 0}
    
    word_to_freq = {k: v for k, v in word_to_freq.items() if v == 0}
    
    word_to_freq = {k: v for k, v in word_to_freq.items() if v == 0}
    
    word_to_freq = {k: v for k, v in word_to_freq.items() if v == 0}
    
    word_to_freq = {k: v for k, v in word_to_freq.items() if v == 0}
    
    word_to_freq = {k: v for k, v in word_to_freq.items() if v == 0}
    
    word_to_freq = {k: v for k, v in word_to_freq.items() if v == 0}
    
    word_to_freq = {k: v for k, v in word_to_freq.items() if v == 0}
    
    word_to_freq = {k: v for k, v in word_to_freq.items() if v == 0}
    
    word_to_freq = {k: v for k, v in word_to_freq.items() if v == 0}
    
    word_to_freq = {k: v for k, v in word_to_freq.items() if v == 0}
    
    word_to_freq = {k: v for k, v in word_to_freq.items() if v == 0}
    
    word_to_freq = {k: v for k, v in word_to_freq.items() if v == 0}
    
    word_to_freq = {k: v for k, v in word_to_freq.items() if v == 0}
    
    word_to_freq = {k: v for k, v in word_to_freq.items() if v == 0}
    
    word_to_freq = {k: v for k, v in word_to_freq.items() if v == 0}
    
    word_to_freq = {k: v for k, v in word_to_freq.items() if v == 0}
    
    word_to_freq