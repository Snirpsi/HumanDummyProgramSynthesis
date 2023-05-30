#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a list of words or converts user input. """    
    
    import sys
    
    if len(sys.argv) > 1:
        words = sys.argv[1:]
    else:
        words = input("Enter words: ")
    
    words = [word.lower() for word in words.split()]
    
    if len(words) == 1:
        words = words[0]
    
    words = [word.upper() for word in words]
    
    print(" ".join(words))
    
