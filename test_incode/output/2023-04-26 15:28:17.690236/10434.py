#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts a list of words. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <words>" % sys.argv[0])
        exit(1)
    
    words = sys.argv[1:]
    
    word_count = len(words)
    
    word_count_per_line = int(word_count / 