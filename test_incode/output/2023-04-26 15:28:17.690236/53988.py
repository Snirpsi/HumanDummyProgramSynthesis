#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores words. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print('usage: wordlist.py words.txt')
        sys.exit()
    
    words = []
    with open(sys.argv[1]) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            words.append(line)
    
    words.sort()
    
    print('\n'.join(words))
    
