#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts a list of words or converts numbers. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python3 wordlist.py words.txt")
        exit(1)
    
    wordlist = sys.argv[1]
    
    with open(wordlist) as words:
        wordlist = words.readlines()
    
    wordlist = [word.strip() for word in wordlist]
    
    wordlist = [word for word in wordlist if word.isalpha()]
    
    wordlist = [word for word in wordlist if word.isdigit()]
    
    wordlist = [word for word in wordlist if word not in ['.', '?', '!']]
    
    wordlist = [word for word in wordlist if word not in ['.', '?', '!', '!', '.', '?', '!']]
    
    wordlist = [word for word in wordlist if word not in ['.', '?', '!', '!', '.', '?', '!', '!']]
    
    wordlist = [word for word in wordlist if word not in ['.', '?', '!', '!', '.', '?', '!', '!']]
    
    wordlist = [word for word in wordlist if word not in ['.', '?', '!', '!', '.', '?', '!', '!']]
    
    wordlist = [word for word in wordlist if word not in ['.', '?', '!', '!', '.', '?', '!', '!']]
    
    wordlist = [word for word in wordlist if word not in ['.', '?', '!', '!', '.', '?', '!', '!']]
    
    wordlist = [word for word in wordlist if word not in ['.', '?', '!', '!', '.', '?', '!', '!']]
    
    wordlist = [word for word in wordlist if word not in ['.', '?', '!', '!', '.', '?', '!', '!']]
    
    wordlist = [word for word in wordlist if word not in ['.', '?', '!', '!', '.', '?', '!', '!']]
    
    wordlist = [word for word in wordlist if word not in ['.', '?', '!', '!', '.', '?', '!', '!']]
    
    wordlist = [word for word in wordlist if word not in ['.', '?', '!', '!', '.', '?', '!', '!']]
    
    wordlist = [word for word in wordlist if word not in ['.', '?', '!', '!', '.', '?', '!', '!']]
    
    wordlist = [word for word in wordlist if word not in ['.', '?', '!', '!', '.', '?', '!', '!']]
    
    wordlist = [word for word in wordlist if word not in ['.', '?', '!', '!', '.', '?', '!', '!']]
    
    wordlist = [word for word in wordlist if 