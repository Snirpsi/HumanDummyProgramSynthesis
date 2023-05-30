#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts words. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <word>" % sys.argv[0])
        sys.exit()
    
    word = sys.argv[1]
    
    words = [word.upper()]
    
    for letter in word:
        if letter.isalpha():
            words.append(letter)
    
    words.sort()
    
    print("\n".join("%s %s" % (word, word) for word in words))
    
