#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a list of words. """    
    import sys
    
    if len(sys.argv) < 2:
        print("usage: python wordlist.py words.txt")
        sys.exit()
    
    words = []
    for line in open(sys.argv[1]):
        words.append(line.strip())
    
    wordlist = " ".join(words)
    
    webserver