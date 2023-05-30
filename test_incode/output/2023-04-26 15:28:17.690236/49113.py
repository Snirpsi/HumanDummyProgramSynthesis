#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a list of words. """    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <words>" % sys.argv[0])
        sys.exit(1)
    
    words = []
    for arg in sys.argv[1:]:
        words.append(arg)
    
    words.sort()
    
    word_counts = {}
    for word in words:
        word_counts[word] = 0
    
    for word in words:
        word_counts[word] += 1
    
    word_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
    
    for word, count in word_counts:
        print("%s: %d" % (word, count))
    
