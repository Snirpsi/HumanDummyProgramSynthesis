#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens words. """    
    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: python3 wordlist.py words.txt")
        exit(1)
    
    words = []
    
    with open(sys.argv[1]) as words:
        for line in words:
            line = line.strip()
            words.append(line)
    
    words.sort()
    
    print("\n".join(words))
    
