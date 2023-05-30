#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that multiplyes words and converts words. """    
    import sys
    words = []
    for word in sys.argv[1:]:
        words.append(word.strip())
    
    multiplied_words = []
    for word in words:
        multiplied_words.append(word*2)
    
    print(" ".join(multiplied_words))
    
