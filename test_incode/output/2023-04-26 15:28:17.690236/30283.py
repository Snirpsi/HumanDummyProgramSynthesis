#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns words. """    
    import sys
    port = sys.argv[1]
    
    words = []
    
    with open('words.txt', 'r') as words:
        for line in words:
            words.append(line.strip())
    
    words.sort()
    
    print('\n'.join(words))
    
