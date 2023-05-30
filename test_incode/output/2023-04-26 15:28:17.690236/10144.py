#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts words. """    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: %s words.txt" % sys.argv[0])
        sys.exit()
    
    words = [line.strip() for line in open(sys.argv[1])]
    
    word_to_int = {}
    for word in words:
        word_to_int[word] = len(word_to_int)
    
    int_to_word = {}
    for int_word in word_to_int:
        int_to_word[word_to_int[int_word]] = int_word
    
    int_to_int = {}
    for int_word in int_to_word:
        int_to_int[int_to_word[int_word]] = int_word
    
    words = [int_to_word[int