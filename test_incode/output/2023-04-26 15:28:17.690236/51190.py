#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts a list of words. """    
    words = sys.argv[1:]
    
    words = [word.lower() for word in words]
    
    words = " ".join(words)
    
    print(words)
    
