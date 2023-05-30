#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints words and removes numbers. """    
    
    words = input("Enter a word: ")
    words = words.split()
    
    for word in words:
        if word.isdigit():
            print(word, end=" ")
        else:
            print(word, end="")
            
    print("\n")
    
