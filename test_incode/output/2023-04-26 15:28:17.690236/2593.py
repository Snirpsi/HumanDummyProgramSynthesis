#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates words and adds all ports. """    
    
    words = []
    
    while True:
        word = input("Enter a word: ")
        
        if word == 'quit':
            break
        
        words.append(word)
    
    for word in words:
        
        print(word)
        
        port = input("Enter a port number: ")
        
        if port == 'quit':
            break
        
        port = int(port)
        
        