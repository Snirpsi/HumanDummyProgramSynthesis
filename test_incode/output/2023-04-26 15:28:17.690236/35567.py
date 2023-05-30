#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts a list of words. """    
    import sys
    words = sys.argv[1:]
    words = [word.strip() for word in words]
    
    word_counts = Counter(words)
    
    for word, count in word_counts.items():
        print('%s: %d' % (word, count))
        
