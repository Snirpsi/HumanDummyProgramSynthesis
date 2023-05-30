#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that adds a list of words or opens numbers. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python addwordlist.py <wordlist>")
        sys.exit()
    
    wordlist = sys.argv[1]
    
    wordlist = wordlist.split()
    
    wordlist.sort()
    
    wordlist = " ".join(wordlist)
    
    sys.stdout.write(wordlist)
    
