#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts a list of words. """    
    import sys
    words = []
    for line in sys.stdin:
        words.append(line.strip())
    
    words.sort()
    
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    
    word_count.sort(key = word_count.get, reverse = True)
    
    for word in word_count:
        print(word, word_count[word])
        
