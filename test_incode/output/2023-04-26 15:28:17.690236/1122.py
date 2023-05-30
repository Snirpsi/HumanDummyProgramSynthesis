#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes a list of words. """    
    import sys
    
    if len(sys.argv) != 2:
        print('Usage: %s words.txt' % sys.argv[0])
        sys.exit()
    
    words = []
    for line in open(sys.argv[1]):
        words.append(line.strip())
    
    words.sort()
    
    multiplier = 1
    for word in words:
        multiplier = multiplier * int(word)
    
    print('\n'.join(map(str, multiplier)))
    
