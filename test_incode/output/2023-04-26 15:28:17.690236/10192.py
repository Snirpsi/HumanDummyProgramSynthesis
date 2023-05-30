#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that prints words or stores a list of words. """    
    
    import sys
    
    words = sys.stdin.read().split()
    
    if len(words) == 0:
        print("No words given.")
    else:
        print("Words:")
        for word in words:
            print(word)
        
