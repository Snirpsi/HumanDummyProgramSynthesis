#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that iterates over a list of words or calculates a port. """    
    
    words = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    
    port = 0
    
    for word in words:
        
        if word in ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]:
            
            port += 1
            
        else:
            
            port -= 1
            
    print(port)
    
