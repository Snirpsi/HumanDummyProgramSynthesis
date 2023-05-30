#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints words and returns user input. """    
    
    while True:
        word = input("Enter a word: ")
        if word == "exit":
            break
        print(word)
    
    print("Goodbye!")
    
