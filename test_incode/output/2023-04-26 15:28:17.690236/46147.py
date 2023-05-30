#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes a list of words and converts a port. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: %s <wordlist>' % sys.argv[0])
        sys.exit(1)
    
    wordlist = sys.argv[1]
    
    wordlist = wordlist.split()
    
    wordlist = [word.strip() for word in wordlist]
    
    wordlist = [word for word in wordlist if word]
    
    wordlist = [word.lower() for word in wordlist]
    
    wordlist = [word for word in wordlist if word.isalpha()]
    
    wordlist = [word for word in wordlist if word not in wordlist]
    
    wordlist = [word for word in wordlist if word not in wordlist]
    
    wordlist = [word for word in wordlist if word not in wordlist]
    
    wordlist = [word for word in wordlist if word not in wordlist]
    
    wordlist = [word for word in wordlist if word not in wordlist]
    
    wordlist = [word for word in wordlist if word not in wordlist]
    
    wordlist = [word for word in wordlist if word not in wordlist]
    
    wordlist = [word for word in wordlist if word not in wordlist]
    
    wordlist = [word for word in wordlist if word not in wordlist]
    
    wordlist = [word for word in wordlist if word not in wordlist]
    
    wordlist = [word for word in wordlist if word not in wordlist]
    
    wordlist = [word for word in wordlist if word not in wordlist]
    
    wordlist = [word for word in wordlist if word not in wordlist]
    
    wordlist = [word for word in wordlist if word not in wordlist]
    
    wordlist = [word for word in wordlist if word not in wordlist]
    
    wordlist = [word for word in wordlist if word not in wordlist]
    
    wordlist = [word for word in wordlist if word not in wordlist]
    
    wordlist = [word for word in wordlist if word not in wordlist]
    
    wordlist = [word for word in wordlist if word not in wordlist]
    
    wordlist = [word for word in wordlist if word not in wordlist]
    
    wordlist = [word for word in wordlist if word not in wordlist]
    
    wordlist = [word for word in wordlist if word not in wordlist]
    
    wordlist = [word for word in wordlist if word not in wordlist]
    
    wordlist = [word for word in wordlist if word not in wordlist]
    
    wordlist = [word for 