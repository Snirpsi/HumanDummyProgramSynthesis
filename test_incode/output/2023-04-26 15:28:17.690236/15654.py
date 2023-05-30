#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts a list of words. """    
    import sys
    
    wordlist = sys.argv[1:]
    
    wordlist = list(map(str.strip, wordlist))
    
    wordlist = list(filter(lambda word: len(word) > 0, wordlist))
    
    wordlist = list(filter(lambda word: len(word) <= 3, wordlist))
    
    wordlist = list(filter(lambda word: len(word) == 3, wordlist))
    
    wordlist = list(filter(lambda word: len(word) == 4, wordlist))
    
    wordlist = list(filter(lambda word: len(word) == 5, wordlist))
    
    wordlist = list(filter(lambda word: len(word) == 6, wordlist))
    
    wordlist = list(filter(lambda word: len(word) == 7, wordlist))
    
    wordlist = list(filter(lambda word: len(word) == 8, wordlist))
    
    wordlist = list(filter(lambda word: len(word) == 9, wordlist))
    
    wordlist = list(filter(lambda word: len(word) == 10, wordlist))
    
    wordlist = list(filter(lambda word: len(word) == 11, wordlist))
    
    wordlist = list(filter(lambda word: len(word) == 12, wordlist))
    
    wordlist = list(filter(lambda word: len(word) == 13, wordlist))
    
    wordlist = list(filter(lambda word: len(word) == 14, wordlist))
    
    wordlist = list(filter(lambda word: len(word) == 15, wordlist))
    
    wordlist = list(filter(lambda word: len(word) == 16, wordlist))
    
    wordlist = list(filter(lambda word: len(word) == 17, wordlist))
    
    wordlist = list(filter(lambda word: len(word) == 18, wordlist))
    
    wordlist = list(filter(lambda word: len(word) == 19, wordlist))
    
    wordlist = list(filter(lambda word: len(word) == 20, wordlist))
    
    wordlist = list(filter(lambda word: len(word) == 21, wordlist))
    
    wordlist = list(filter(lambda word: len(word) == 22, wordlist))
    
    wordlist = list(filter(lambda word: len(word) == 23, wordlist))
    
    wordlist = list(filter(lambda word: len(word) == 24, wordlist))
    
    wordlist = list(filter(lambda word: len(word) == 25, wordlist))
    
    wordlist = list(filter(lambda word: len(word) == 26, wordlist))
    
    wordlist = list(filter(lambda word: len(word) == 27, wordlist))
    
    wordlist = list(filter(lambda word: len(word) == 28, wordlist))
    
    wordlist = list(filter(lambda word: len(word) == 29, wordlist))
    
    wordlist = list(filter(lambda word: len(word) == 30, wordlist))
    
    wordlist = list(filter(lambda word