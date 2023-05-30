#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that multiplyes numbers and adds a list of words. """    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python wordlist.py wordlist.txt")
        exit(1)
    
    wordlist = sys.argv[1].split()
    
    wordlist.sort()
    
    wordlist.extend(sys.argv[2:])
    
    wordlist.sort()
    
    print(" ".join(wordlist))
    
