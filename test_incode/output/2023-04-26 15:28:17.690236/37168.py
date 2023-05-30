#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that calculates words. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <words>" % sys.argv[0])
        exit(1)
    
    words = sys.argv[1:]
    
    words = [word.strip() for word in words]
    
    word_count = len(words)
    
    word_count_per_line = int(word_count / 