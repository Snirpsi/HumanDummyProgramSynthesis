#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates user input or converts words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        words = []
        for word in sys.argv[1:]:
            words.append(word)
    else:
        words = input("Enter words: ")
    
    print(words)
    
    for word in words:
        print(word)
    
