#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens words or enumerates a list of words. """    
    
    import sys
    
    if len(sys.argv) == 1:
        print('Usage: python wordlist.py <words>')
        sys.exit()
    
    words = sys.argv[1:]
    
    for word in words:
        word = word.strip()
        
        if word:
            print(word)
        else:
            print('No words found')
    
