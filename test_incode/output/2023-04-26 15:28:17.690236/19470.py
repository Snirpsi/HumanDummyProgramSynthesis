#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts words and calculates user input. """    
    
    wordlist = input("Enter a wordlist separated by spaces (no spaces between words): ")
    
    wordlist = wordlist.split()
    
    wordlist = list(map(lambda word: word.lower(), wordlist))
    
    wordlist = list(filter(lambda word: word not in stopwords, wordlist))
    
    wordlist = list(filter(lambda word: len(word) > 2, wordlist))
    
    wordlist = list(filter(lambda word: len(word) < 5, wordlist))
    
    wordlist = list(filter(lambda word: len(word) > 5, wordlist))
    
    wordlist = list(filter(lambda word: len(word) < 10, wordlist))
    
    wordlist = list(filter(lambda word: len(word) > 10, wordlist))
    
    wordlist = list(filter(lambda word: len(word) < 15, wordlist))
    
    wordlist = list(filter(lambda word: len(word) > 15, wordlist))
    
    wordlist = list(filter(lambda word: len(word) < 20, wordlist))
    
    wordlist = list(filter(lambda word: len(word) > 20, wordlist))
    
    wordlist = list(filter(lambda word: len(word) < 25, wordlist))
    
    wordlist = list(filter(lambda word: len(word) > 25, wordlist))
    
    wordlist = list(filter(lambda word: len(word) < 30, wordlist))
    
    wordlist = list(filter(lambda word: len(word) > 30, wordlist))
    
    wordlist = list(filter(lambda word: len(word) < 35, wordlist))
    
    wordlist = list(filter(lambda word: len(word) > 35, wordlist))
    
    wordlist = list(filter(lambda word: len(word) < 40, wordlist))
    
    wordlist = list(filter(lambda word: len(word) > 40, wordlist))
    
    wordlist = list(filter(lambda word: len(word) < 45, wordlist))
    
    wordlist = list(filter(lambda word: len(word) > 45, wordlist))
    
    wordlist = list(filter(lambda word: len(word) < 50, wordlist))
    
    wordlist = list(filter(lambda word: len(word) > 50, wordlist))
    
    wordlist = list(filter(lambda word: len(word) < 55, wordlist))
    
    wordlist = list(filter(lambda word: len(word) > 55, wordlist))
    
    wordlist = list(filter(lambda word: len(word) < 60, wordlist))
    
    wordlist = list(filter(lambda word: len(word) > 60, wordlist))
    
    wordlist = list(filter(lambda word: len(word) < 65, wordlist))
    
    wordlist = list(filter(lambda word: len(word) > 65, wordlist))
    
    wordlist = list(filter(lambda word: len(word) < 70, wordlist))
    
    