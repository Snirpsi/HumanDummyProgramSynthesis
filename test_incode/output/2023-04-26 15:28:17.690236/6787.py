#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates words and removes words. """    
    
    words = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    
    words = [word.lower() for word in words]
    
    words = [word for word in words if word not in words]
    
    print(words)
    
