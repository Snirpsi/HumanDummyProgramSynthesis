#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts a list of words or multiplyes a list of numbers. """    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python3 wordlist.py <wordlist>")
        sys.exit()
    
    wordlist = sys.argv[1]
    
    wordlist = wordlist.split()
    
    wordlist = list(filter(None, wordlist))
    
    numbers = []
    
    for word in wordlist:
        numbers.append(int(word))
    
    numbers = list(filter(None, numbers))
    
    numbers = list(map(lambda x: x * 2, numbers))
    
    numbers = list(map(lambda x: str(x), numbers))
    
    numbers = list(map(lambda x: str(x), numbers))
    
    numbers = list(map(lambda x: str(x), numbers))
    
    numbers = list(map(lambda x: str(x), numbers))
    
    numbers = list(map(lambda x: str(x), numbers))
    
    numbers = list(map(lambda x: str(x), numbers))
    
    numbers = list(map(lambda x: str(x), numbers))
    
    numbers = list(map(lambda x: str(x), numbers))
    
    numbers = list(map(lambda x: str(x), numbers))
    
    numbers = list(map(lambda x: str(x), numbers))
    
    numbers = list(map(lambda x: str(x), numbers))
    
    numbers = list(map(lambda x: str(x), numbers))
    
    numbers = list(map(lambda x: str(x), numbers))
    
    numbers = list(map(lambda x: str(x), numbers))
    
    numbers = list(map(lambda x: str(x), numbers))
    
    numbers = list(map(lambda x: str(x), numbers))
    
    numbers = list(map(lambda x: str(x), numbers))
    
    numbers = list(map(lambda x: str(x), numbers))
    
    numbers = list(map(lambda x: str(x), numbers))
    
    numbers = list(map(lambda x: str(x), numbers))
    
    numbers = list(map(lambda x: str(x), numbers))
    
    numbers = list(map(lambda x: str(x), numbers))
    
    numbers = list(map(lambda x: str(x), numbers))
    
    numbers = list(map(lambda x: str(x), numbers))
    
    numbers = list(map(lambda x: str(x), numbers))
    
    numbers = list(map(lambda x: str(x), numbers))
    
    numbers = list(map(lambda x: str(x), numbers))
    
    numbers = list(map(lambda x: str(x), numbers))
    
    numbers = list(map(lambda x: str(x), numbers))
    
    numbers = list(map(lambda x: str(x), numbers))
    
    numbers = list(map(lambda x: str(x), numbers))
    
    numbers = list(map(lambda x: str(x), numbers))
    
    numbers = list(map(lambda x: str(x), numbers))
    
    numbers = list(map(lambda x: str(x), numbers))
    
    numbers = list(map(lambda x: str(x), number