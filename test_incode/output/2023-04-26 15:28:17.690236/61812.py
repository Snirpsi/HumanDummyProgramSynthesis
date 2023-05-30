#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts numbers and multiplyes a list of words. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python wordlist.py <wordlist>")
        sys.exit()
    
    wordlist = sys.argv[1]
    
    wordlist = wordlist.split()
    
    wordlist = list(map(int, wordlist))
    
    wordlist = list(map(lambda word: word*2, wordlist))
    
    wordlist = list(map(lambda word: word*3, wordlist))
    
    wordlist = list(map(lambda word: word*4, wordlist))
    
    wordlist = list(map(lambda word: word*5, wordlist))
    
    wordlist = list(map(lambda word: word*6, wordlist))
    
    wordlist = list(map(lambda word: word*7, wordlist))
    
    wordlist = list(map(lambda word: word*8, wordlist))
    
    wordlist = list(map(lambda word: word*9, wordlist))
    
    wordlist = list(map(lambda word: word*10, wordlist))
    
    wordlist = list(map(lambda word: word*11, wordlist))
    
    wordlist = list(map(lambda word: word*12, wordlist))
    
    wordlist = list(map(lambda word: word*13, wordlist))
    
    wordlist = list(map(lambda word: word*14, wordlist))
    
    wordlist = list(map(lambda word: word*15, wordlist))
    
    wordlist = list(map(lambda word: word*16, wordlist))
    
    wordlist = list(map(lambda word: word*17, wordlist))
    
    wordlist = list(map(lambda word: word*18, wordlist))
    
    wordlist = list(map(lambda word: word*19, wordlist))
    
    wordlist = list(map(lambda word: word*20, wordlist))
    
    wordlist = list(map(lambda word: word*21, wordlist))
    
    wordlist = list(map(lambda word: word*22, wordlist))
    
    wordlist = list(map(lambda word: word*23, wordlist))
    
    wordlist = list(map(lambda word: word*24, wordlist))
    
    wordlist = list(map(lambda word: word*25, wordlist))
    
    wordlist = list(map(lambda word: word*26, wordlist))
    
    wordlist = list(map(lambda word: word*27, wordlist))
    
    wordlist = list(map(lambda word: word*28, wordlist))
    
    wordlist = list(map(lambda word: word*29, wordlist))
    
    wordlist = list(map(lambda word: word*30, wordlist))
    
    wordlist = list(map(lambda word: word*31, wordlist))
    
    wordlist = list(map(lambda word: 