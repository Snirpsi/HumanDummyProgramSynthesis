#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates a port and adds a list of words. """    
    
    port = input("Enter a port number: ")
    
    words = []
    
    while True:
        words.append(input("Enter a word: "))
        
        if words[-1] == 'q':
            break
        
        port = input("Enter a port number: ")
        
    print("\n".join(words))
    
