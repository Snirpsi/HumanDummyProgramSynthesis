#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a list of words or iterates over fruits. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s [words]" % sys.argv[0])
        sys.exit()
    
    words = []
    for arg in sys.argv[1:]:
        if arg == '-':
            words.extend(sys.argv[2:])
        else:
            words.append(arg)
    
    words = list(set(words))
    
    fruits = ['apple', 'banana', 'cherry']
    
    for word in words:
        print("%s: %s" % (word, 