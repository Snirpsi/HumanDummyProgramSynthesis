#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens a list of words or stores a port. """    
    
    port = int(input("Enter a port number: "))
    
    words = []
    
    while True:
        word = input("Enter a word: ")
        
        if word == "":
            break
        
        words.append(word)
    
    words.sort()
    
    