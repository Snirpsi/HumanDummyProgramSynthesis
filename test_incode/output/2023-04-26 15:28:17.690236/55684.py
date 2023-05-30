#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that calculates words and adds a port. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <words>" % sys.argv[0])
        sys.exit(1)
    
    words = sys.argv[1:]
    
    words = [word.strip() for word in words]
    
    word_count = len(words)
    
    word_count_by_port = {}
    
    for word in words:
        word_count_by_port[word] = word_count_by_port.get(word, 0) + 1
    
    word_count_by_port.sort(key=word_count_by_port.get, reverse=True)
    
    for word, count in word_count_by_port.items():
        print("%s: %d" % (word, count))
    
