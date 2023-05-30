#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a list of words. """    
    
    import sys
    
    wordlist = sys.argv[1:]
    
    wordlist = list(map(str.strip, wordlist))
    
    wordlist = list(map(str.split, wordlist))
    
    wordlist = list(map(lambda w: w.lower(), wordlist))
    
    wordlist = list(map(lambda w: w.strip(), wordlist))
    
    wordlist = list(map(lambda w: w.upper(), wordlist))
    
    wordlist = list(map(lambda w: w.capitalize(), wordlist))
    
    wordlist = list(map(lambda w: w.title(), wordlist))
    
    wordlist = list(map(lambda w: w.strip(), wordlist))
    
    wordlist = list(map(lambda w: w.replace('.', ''), wordlist))
    
    wordlist = list(map(lambda w: w.replace(',', ''), wordlist))
    
    wordlist = list(map(lambda w: w.replace(':', ''), wordlist))
    
    wordlist = list(map(lambda w: w.replace(';', ''), wordlist))
    
    wordlist = list(map(lambda w: w.replace('?', ''), wordlist))
    
    wordlist = list(map(lambda w: w.replace('!', ''), wordlist))
    
    wordlist = list(map(lambda w: w.replace(':', ''), wordlist))
    
    wordlist = list(map(lambda w: w.replace(';', ''), wordlist))
    
    wordlist = list(map(lambda w: w.replace(':', ''), wordlist))
    
    wordlist = list(map(lambda w: w.replace('!', ''), wordlist))
    
    wordlist = list(map(lambda w: w.replace(':', ''), wordlist))
    
    wordlist = list(map(lambda w: w.replace(';', ''), wordlist))
    
    wordlist = list(map(lambda w: w.replace('?', '.'), wordlist))
    
    wordlist = list(map(lambda w: w.replace('!', '.'), wordlist))
    
    wordlist = list(map(lambda w: w.replace(':', '.'), wordlist))
    
    wordlist = list(map(lambda w: w.replace(';', '.'), wordlist))
    
    wordlist = list(map(lambda w: w.replace('?', '.'), wordlist))
    
    wordlist = list(map(lambda w: w.replace('!', '.'), wordlist))
    
    wordlist = list(map(lambda w: w.replace(':', '.'), wordlist))
    
    wordlist = list(map(lambda w: w.replace(';', '.'), wordlist))
    
    wordlist = list(map(lambda w: w.replace('?', '.'), wordlist))
    
    wordlist = list(map(lambda w: w.replace('!', '.'), wordlist))
    
    wordlist = list(map(lambda w: w.replace(':