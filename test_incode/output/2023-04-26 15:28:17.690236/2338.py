#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes words. """    
    
    while True:
        word = input("Enter a word: ")
        
        if word == "":
            print("Goodbye!")
            break
        else:
            print(word*