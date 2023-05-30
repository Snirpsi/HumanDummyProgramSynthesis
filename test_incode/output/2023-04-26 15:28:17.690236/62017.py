#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts a list of words. """    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: python wordlist2txt.py <wordlist>")
        sys.exit(1)
    
    wordlist = sys.argv[1]
    
    wordlist = wordlist.split()
    
    wordlist = " ".join(wordlist)
    
    with open('wordlist.txt', 'w') as f:
        f.write(wordlist)
    
    print("Done.")
    
