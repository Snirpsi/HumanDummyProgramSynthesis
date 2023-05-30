#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates a list of words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        wordlist = sys.argv[1]
    else:
        wordlist = input("Enter the wordlist to calculate: ")
    
    wordlist = wordlist.split()
    
    wordlist = list(set(wordlist))
    
    wordlist = list(filter(lambda word: len(word) > 0, wordlist))
    
    wordlist = list(filter(lambda word: word not in wordlist, wordlist))
    
    wordlist = list(filter(lambda word: word not in wordlist, wordlist))
    
    wordlist = list(filter(lambda word: word not in wordlist, wordlist))
    
    wordlist = list(filter(lambda word: word not in wordlist, wordlist))
    
    wordlist = list(filter(lambda word: word not in wordlist, wordlist))
    
    wordlist = list(filter(lambda word: word not in wordlist, wordlist))
    
    wordlist = list(filter(lambda word: word not in wordlist, wordlist))
    
    wordlist = list(filter(lambda word: word not in wordlist, wordlist))
    
    wordlist = list(filter(lambda word: word not in wordlist, wordlist))
    
    wordlist = list(filter(lambda word: word not in wordlist, wordlist))
    
    wordlist = list(filter(lambda word: word not in wordlist, wordlist))
    
    wordlist = list(filter(lambda word: word not in wordlist, wordlist))
    
    wordlist = list(filter(lambda word: word not in wordlist, wordlist))
    
    wordlist = list(filter(lambda word: word not in wordlist, wordlist))
    
    wordlist = list(filter(lambda word: word not in wordlist, wordlist))
    
    wordlist = list(filter(lambda word: word not in wordlist, wordlist))
    
    wordlist = list(filter(lambda word: word not in wordlist, wordlist))
    
    wordlist = list(filter(lambda word: word not in wordlist, wordlist))
    
    wordlist = list(filter(lambda word: word not in wordlist, wordlist))
    
    wordlist = list(filter(lambda word: word not in wordlist, wordlist))
    
    wordlist = list(filter(lambda word: word not in wordlist, wordlist))
    
    wordlist = list(filter(lambda word: word not in wordlist, wordlist))
    
    wordlist = list(filter(lambda word: word not in wordlist, wordlist))
    
    wordlist = list(filter(lambda word: word not in wordlist, wordlist))
    
    wordlist = list(filter(lambda word: word not in wordlist, wordlist))
    
    wordlist = list(filter(lambda word: word not in wordlist, wordlist))
    
    wordlist = list(filter(lambda word: word not in wordlist, wordlist))
    
    wordlist = list(filter(lambda word: word not in wordlist, word