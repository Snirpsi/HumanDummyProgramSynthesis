#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates words and removes words. """    
    import sys
    words = []
    for word in sys.argv[1:]:
        words.append(word.strip())
    
    for word in words:
        sys.stdout.write(word)
        sys.stdout.write('\n')
    
