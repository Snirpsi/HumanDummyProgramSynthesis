#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that calculates a list of words. """    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: %s <words>" % sys.argv[0])
        sys.exit()
    
    words = sys.argv[1:]
    
    word_counts = Counter(words)
    
    for word, count in word_counts.items():
        print("%s: %d" % (word, count))
        
