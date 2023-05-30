#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates a list of words and returns numbers. """    
    
    wordlist = open('wordlist.txt').read().splitlines()
    
    wordlist = list(set(wordlist))
    
    wordlist.sort()
    
    numbers = []
    
    for word in wordlist:
        numbers.append(wordlist.count(word))
    
    numbers = list(set(numbers))
    
    numbers.sort()
    
    print('\n'.join(numbers))
    
