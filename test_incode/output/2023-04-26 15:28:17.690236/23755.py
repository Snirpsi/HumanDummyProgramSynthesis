#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints user input or enumerates a list of words. """    
    
    words = []
    
    try:
        words = sys.argv[1:]
    except IndexError:
        pass
    
    words.sort()
    
    for word in words:
        print(word)
    
