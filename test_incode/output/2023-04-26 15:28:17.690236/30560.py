#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes a list of numbers or iterates over words. """    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: python3 remove.py <word>')
        sys.exit()
    
    word = sys.argv[1]
    
    removed = []
    
    for word in remove:
        if word in word:
            removed.append(word)
    
    print('\n'.join(removed))
    
