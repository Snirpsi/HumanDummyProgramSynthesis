#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that adds numbers and multiplyes a list of words. """    
    
    import sys
    
    wordlist = sys.argv[1:]
    
    wordlist = wordlist[0].split()
    
    wordlist = list(map(int, wordlist))
    
    wordlist = list(map(lambda word: word * 2, wordlist))
    
    wordlist = list(map(lambda word: word + 2, wordlist))
    
    wordlist = list(map(lambda word: word - 2, wordlist))
    
    wordlist = list(map(lambda word: word + 3, wordlist))
    
    wordlist = list(map(lambda word: word - 3, wordlist))
    
    wordlist = list(map(lambda word: word * 3, wordlist))
    
    wordlist = list(map(lambda word: word + 3, wordlist))
    
    wordlist = list(map(lambda word: word - 3, wordlist))
    
    wordlist = list(map(lambda word: word * 4, wordlist))
    
    wordlist = list(map(lambda word: word + 4, wordlist))
    
    wordlist = list(map(lambda word: word - 4, wordlist))
    
    wordlist = list(map(lambda word: word * 5, wordlist))
    
    wordlist = list(map(lambda word: word + 5, wordlist))
    
    wordlist = list(map(lambda word: word - 5, wordlist))
    
    wordlist = list(map(lambda word: word * 6, wordlist))
    
    wordlist = list(map(lambda word: word + 6, wordlist))
    
    wordlist = list(map(lambda word: word - 6, wordlist))
    
    wordlist = list(map(lambda word: word * 7, wordlist))
    
    wordlist = list(map(lambda word: word + 7, wordlist))
    
    wordlist = list(map(lambda word: word - 7, wordlist))
    
    wordlist = list(map(lambda word: word * 8, wordlist))
    
    wordlist = list(map(lambda word: word + 8, wordlist))
    
    wordlist = list(map(lambda word: word - 8, wordlist))
    
    wordlist = list(map(lambda word: word * 9, wordlist))
    
    wordlist = list(map(lambda word: word + 9, wordlist))
    
    wordlist = list(map(lambda word: word - 9, wordlist))
    
    wordlist = list(map(lambda word: word * 10, wordlist))
    
    wordlist = list(map(lambda word: word + 10, wordlist))
    
    wordlist = list(map(lambda word: word - 10, wordlist))
    
    wordlist = list(map(lambda word: word * 11, wordlist))
    
    wordlist = list(map(lambda word: word + 11, wordlist))
    
    wordlist = list(map(lambda word: word - 11, word