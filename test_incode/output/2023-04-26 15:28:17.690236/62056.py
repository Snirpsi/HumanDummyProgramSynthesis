#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over words. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print('usage: python wordlist.py <wordlist>')
        sys.exit()
    
    wordlist = sys.argv[1]
    
    words = []
    
    with open(wordlist) as wordlist_file:
        for line in wordlist_file:
            line = line.strip()
            
            if line:
                words.append(line)
    
    words.sort()
    
    print('\n'.join(words))
    
