#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a list of words and prints a list of numbers. """    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python wordlist.py words.txt")
        sys.exit()
    
    wordlist = sys.argv[1].split()
    
    numbers = []
    
    for word in wordlist:
        numbers.append(int(word))
    
    print(numbers)
    
