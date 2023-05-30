#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates a list of words. """    
    words = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    word_counter = collections.Counter(words)
    
    for word, count in word_counter.items():
        print('%s: %d' % (word, count))
        
