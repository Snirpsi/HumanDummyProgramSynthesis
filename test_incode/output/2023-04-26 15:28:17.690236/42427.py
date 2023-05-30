#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that prints words. """    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: python wordlist.py words.txt')
        sys.exit()
    
    wordlist = sys.argv[1]
    
    with open(wordlist, 'r') as wordfile:
        words = [word.strip() for word in wordfile]
    
    print('\n'.join(words))
    
