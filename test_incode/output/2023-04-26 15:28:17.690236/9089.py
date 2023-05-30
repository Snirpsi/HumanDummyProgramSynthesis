#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints words and converts words. """    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: python wordlist.py <wordlist>")
        sys.exit()
    
    wordlist = sys.argv[1]
    
    words = []
    
    with open(wordlist) as f:
        for line in f:
            line = line.strip()
            
            if line:
                words.append(line)
    
    words.sort()
    
    print("\n".join(words))
    
