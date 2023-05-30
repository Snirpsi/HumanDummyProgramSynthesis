#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes numbers or enumerates words. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: %s <word>' % sys.argv[0])
        sys.exit()
    
    word = sys.argv[1]
    
    # Do the multiplication
    word = int(word)
    
    # Do the enumeration
    words = [word]
    
    for letter in word:
        words.append(letter * word)
    
    print(''.join(words))
    
