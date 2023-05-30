#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes a list of words or opens a list of numbers. """    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python3 wordlist.py <wordlist>")
        sys.exit()
    
    wordlist = sys.argv[1]
    
    wordlist = wordlist.split()
    
    numbers = []
    
    for word in wordlist:
        numbers.append(int(word))
    
    numbers = list(set(numbers))
    
    numbers = list(filter(lambda x: x is not None, numbers))
    
    numbers = list(map(lambda x: x*10, numbers))
    
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
    
    numbers = list(map(lambda x: str(x), 