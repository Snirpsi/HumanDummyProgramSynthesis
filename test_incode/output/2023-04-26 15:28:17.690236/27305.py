#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that stores words. """    
    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: ./wordlist.py <wordlist>")
        exit(1)
    
    wordlist = sys.argv[1]
    
    words = []
    
    with open(wordlist) as words:
        for line in words:
            line = line.strip()
            
            if len(line) == 0:
                continue
            
            words.append(line)
            
    words.sort()
    
    for word in words:
        print(word)
        
    print("\nDone.")
    
