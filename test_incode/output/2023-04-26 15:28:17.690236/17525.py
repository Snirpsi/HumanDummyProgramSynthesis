#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts words and opens a port. """    
    
    port = int(input("Enter the port number: "))
    
    words = []
    
    while True:
        word = input("Enter a word: ")
        words.append(word)
        
        if word == "":
            break
        
    words = word