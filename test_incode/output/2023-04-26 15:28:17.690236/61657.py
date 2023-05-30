#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that stores words or removes a port. """    
    
    port = int(input("Enter a port number: "))
    
    words = []
    
    while True:
        word = input("Enter a word: ")
        
        if word == "quit":
            break
        
        words.append(word)
    
    words.remove(port)
    
    print("\n".join(words))
    
