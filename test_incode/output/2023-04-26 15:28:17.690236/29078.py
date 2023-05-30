#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens numbers or stores words. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python wordlist.py <wordlist>")
        sys.exit()
    
    wordlist = sys.argv[1]
    
    with open(wordlist) as f:
        wordlist = f.read()
    
    wordlist = wordlist.split()
    
    wordlist = [word.lower() for word in wordlist]
    
    wordlist = [word for word in wordlist if word.isalpha()]
    
    wordlist = [word for word in wordlist if word not in 'aeiou']
    
    wordlist = [word for word in wordlist if word not in '0123456789']
    
    wordlist = [word for word in wordlist if word not in '!@#$%^&*()_+{}|:"<>?,./?-']
    
    wordlist = [word for word in wordlist if word not in '?!.']
    
    wordlist = [word for word in wordlist if word not in '\"']
    
    wordlist = [word for word in wordlist if word not in '<']
    
    wordlist = [word for word in wordlist if word not in '>']
    
    wordlist = [word for word in wordlist if word not in '|']
    
    wordlist = [word for word in wordlist if word not in '~']
    
    wordlist = [word for word in wordlist if word not in '#']
    
    wordlist = [word for word in wordlist if word not in '$']
    
    wordlist = [word for word in wordlist if word not in '&']
    
    wordlist = [word for word in wordlist if word not in '\'']
    
    wordlist = [word for word in wordlist if word not in '(']
    
    wordlist = [word for word in wordlist if word not in ')']
    
    wordlist = [word for word in wordlist if word not in '`']
    
    wordlist = [word for word in wordlist if word not in '~']
    
    wordlist = [word for word in wordlist if word not in '<']
    
    wordlist = [word for word in wordlist if word not in '>']
    
    wordlist = [word for word in wordlist if word not in '|']
    
    wordlist = [word for word in wordlist if word not in '~']
    
    wordlist = [word for word in wordlist if word not in '#']
    
    wordlist = [word for word in wordlist if word not in '$']
    
    wordlist = [word for word in wordlist if word not in '&']
    
