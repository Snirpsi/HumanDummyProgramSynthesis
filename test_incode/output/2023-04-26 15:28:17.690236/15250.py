#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens a list of words and removes a port. """    
    words = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    port = "80"
    
    for word in words:
        if word.startswith(port):
            word = word.replace(port, "")
            print(word)
            
        else:
            print(word)
            
