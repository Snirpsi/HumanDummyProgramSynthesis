#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens user input or enumerates words. """    
    
    word = input("Enter a word: ")
    
    if word == "exit":
        print("Goodbye!")
        exit()
    
    if word == "quit":
        print("Goodbye!")
        quit()
    
    if word == "help":
        print("This program will enumerate words in a text file.")
        print("Type 'quit' to quit.")
        exit()
    
    words = open(word, "r")
    
    for line in words:
        print(line)
        
    words.close()
    
