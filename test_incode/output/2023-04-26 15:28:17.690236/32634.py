#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates a list of words or prints numbers. """    
    
    words = ["cat", "dog", "mouse", "bird"]
    
    while True:
        
        # Print the list of words or the number
        if words:
            print(words)
        else:
            print(