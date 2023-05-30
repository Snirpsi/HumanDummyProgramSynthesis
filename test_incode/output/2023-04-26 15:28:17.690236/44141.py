#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds words or calculates words. """    
    
    while True:
        word = input("Enter a word: ")
        
        if word == "quit":
            break
        
        if word == "add":
            print(word + " was added.")
        
        elif word == "calc":
            print(word + " was calculated.")
        
        else:
            print("Invalid input.")
    
