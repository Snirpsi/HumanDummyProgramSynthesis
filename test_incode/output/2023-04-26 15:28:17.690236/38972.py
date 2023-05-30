#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that stores user input and converts a list of words. """    
    
    # Get the list of words from the user
    words = []
    
    # Get the words from the user
    while True:
        word = input("Enter a word: ")
        words.append(word)
        
        # Check if the user wants to quit
        if word == "quit":
            break
    
    # Convert the words to lowercase
    words = [word.lower() for word in words]
    
    # Print the converted words
    print("\n".join(words))
    
