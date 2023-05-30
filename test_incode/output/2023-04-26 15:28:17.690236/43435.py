#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts words or enumerates fruits. """    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: python wordlist.py [words]')
        sys.exit()
    
    words = sys.argv[1:]
    
    for word in words:
        word = word.strip()
        
        if word:
            print(word)
        else:
            print('')
    
