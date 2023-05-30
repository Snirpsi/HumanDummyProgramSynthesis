#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes a list of words and converts all ports. """    
    import sys
    
    wordlist = sys.argv[1:]
    
    wordlist = [word.strip() for word in wordlist]
    
    wordlist = list(set(wordlist))
    
    wordlist = [word for word in wordlist if word.isalpha()]
    
    wordlist = list(set(wordlist))
    
    wordlist = [word for word in wordlist if word.isdigit()]
    
    wordlist = list(set(wordlist))
    
    wordlist = [word for word in wordlist if word.isalnum()]
    
    wordlist = list(set(wordlist))
    
    wordlist = [word for word in wordlist if word not in wordlist]
    
    wordlist = list(set(wordlist))
    
    wordlist = [word for word in wordlist if word not in wordlist]
    
    wordlist = list(set(wordlist))
    
    wordlist = [word for word in wordlist if word not in wordlist]
    
    wordlist = list(set(wordlist))
    
    wordlist = [word for word in wordlist if word not in wordlist]
    
    wordlist = list(set(wordlist))
    
    wordlist = [word for word in wordlist if word not in wordlist]
    
    wordlist = list(set(wordlist))
    
    wordlist = [word for word in wordlist if word not in wordlist]
    
    wordlist = list(set(wordlist))
    
    wordlist = [word for word in wordlist if word not in wordlist]
    
    wordlist = list(set(wordlist))
    
    wordlist = [word for word in wordlist if word not in wordlist]
    
    wordlist = list(set(wordlist))
    
    wordlist = [word for word in wordlist if word not in wordlist]
    
    wordlist = list(set(wordlist))
    
    wordlist = [word for word in wordlist if word not in wordlist]
    
    wordlist = list(set(wordlist))
    
    wordlist = [word for word in wordlist if word not in wordlist]
    
    wordlist = list(set(wordlist))
    
    wordlist = [word for word in wordlist if word not in wordlist]
    
    wordlist = list(set(wordlist))
    
    wordlist = [word for word in wordlist if word not in wordlist]
    
    wordlist = list(set(wordlist))
    
    wordlist = [word for word in wordlist if word not in wordlist]
    
    wordlist = list(set(wordlist))
    
    wordlist = [word for word in wordlist if word not in wordlist]
    
    word