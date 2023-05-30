#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens words or enumerates words. """    
    
    words = []
    
    for word in sys.argv[1:]:
        if word == '-':
            words.append(word)
        else:
            words.append(word.lower())
    
    words.sort()
    
    for word in words:
        print(word)
        
    sys.exit(0)
    
