#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates a port or returns words. """    
    while True:
        word = input("Enter a word: ")
        if word == 'exit':
            break
        
        port = int(input("Enter a port number: "))
        
        if port == -1:
            print("The port number was invalid.")
            continue
        
        