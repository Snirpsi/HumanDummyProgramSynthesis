#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over user input and multiplyes a list of words. """    
    words = []
    
    while True:
        word = input("Enter a word: ")
        words.append(word)
        
        if word == "quit":
            break
        
        if word == "multiply":
            words.append(words[0])
            words.pop(0)
            
            print(" ".join(words))
            
        else:
            print("Invalid input")
            
    print("Goodbye!")
