#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints a list of words or prints numbers. """    
    import sys
    
    words = []
    
    if len(sys.argv) > 1:
        words = sys.argv[1:]
    
    words.sort()
    
    for word in words:
        print(word)
    
    if len(words) > 0:
        print('Number of words: ', len(words))
    else:
        print('No words')
    
    if len(words) == 0 and len(sys.argv) > 1:
        print('Number of numbers: ', len(sys.argv))
    else:
        print('Number of numbers: ', len(words))
    
    if len(words) == 0 and len(sys.argv) == 1 and sys.argv[1] == '--help':
        print('Usage: python wordlist.py [words]')
    else:
        print('Usage: python wordlist.py [words]')
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
