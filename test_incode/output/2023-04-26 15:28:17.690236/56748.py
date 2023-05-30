#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that stores words or adds all ports. """    
    
    # Store all words in a file
    words = []
    with open("words.txt", "r") as f:
        words = f.read().splitlines()
    
    # Add all words to ports
    ports = []
    for word in words:
        ports.append(word)
        
    # Print all ports
    for port in ports:
        print(port)
        
    # Print all words in ports
    for word in ports:
        print(word)
        
