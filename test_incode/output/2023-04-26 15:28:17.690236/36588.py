#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens a list of words and calculates a port. """    
    words = []
    
    words.append("hello")
    words.append("world")
    
    port = 0
    
    for word in words:
        port += word.count("o")
        
    print(port)
    
