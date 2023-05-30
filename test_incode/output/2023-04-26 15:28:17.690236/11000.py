#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that removes words and opens user input. """    
    
    words = input("Enter a word: ")
    
    words = words.split()
    
    for word in words:
        word = word.strip()
        
        if word != "":
            print(word)
        else:
            print("No word found")
    
