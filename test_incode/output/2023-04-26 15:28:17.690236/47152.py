#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens a port or multiplyes a list of words. """    
    
    port = int(input("Enter a port number: "))
    
    words = []
    
    while True:
        word = input("Enter a word: ")
        words.append(word)
        
        if word == "q":
            break
        
    words = list(set(words))
    
    multiplied = []
    
    for word in words:
        multiplied.append(word*