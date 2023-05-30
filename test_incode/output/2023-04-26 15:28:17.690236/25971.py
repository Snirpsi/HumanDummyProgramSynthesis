#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates words or multiplyes words. """    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: %s word" % sys.argv[0])
        sys.exit()
    
    word = sys.argv[1]
    
    words = []
    
    for char in word:
        if char.isalpha():
            words.append(char)
        else:
            words.append(char*2)
    
    print("\n".join(words))
    
