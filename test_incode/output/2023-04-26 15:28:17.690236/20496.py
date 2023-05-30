#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates words and adds user input. """    
    words = []
    
    while True:
        word = input("Enter a word: ")
        words.append(word)
        
        if word == "q":
            break
        
    print("\n".join("