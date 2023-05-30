#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes a list of words. """    
    
    import sys
    
    if len(sys.argv) != 2:
        sys.exit('Usage: %s words.txt' % sys.argv[0])
    
    words = []
    for line in open(sys.argv[1]):
        line = line.strip()
        words.append(line)
    
    words.sort()
    
    print('\n'.join(words))
    
