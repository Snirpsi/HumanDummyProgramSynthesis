#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts words and calculates a list of words. """    
    import sys
    
    words = []
    for line in sys.stdin:
        line = line.strip()
        if line:
            words.append(line)
    
    words.sort()
    
    words_to_count = {}
    for word in words:
        if word in words_to_count:
            words_to_count[word] += 1
        else:
            words_to_count[word] = 1
    
    words_to_count = [word for word in words_to_count if words_to_count[word] > 1]
    
    for word in words_to_count:
        print(word, "