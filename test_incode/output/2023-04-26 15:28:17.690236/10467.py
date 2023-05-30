#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints words. """    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: %s words.txt' % sys.argv[0])
        sys.exit()
    
    with open(sys.argv[1]) as f:
        for word in f.read().split():
            print(word)
    
