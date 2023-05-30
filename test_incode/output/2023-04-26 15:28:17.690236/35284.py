#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that adds words or adds user input. """    
    
    # Get the input from the user
    user_input = input("Enter a word: ")
    
    # Check if the word is valid
    if user_input == "exit":
        sys.exit()
    
    # Add the word to the dictionary
    dictionary = add_word(user_input)
    
    # Print the dictionary
    print(dictionary)
    
    # Print the word that was added
    print(dictionary[user_input])
    
    # Print the word that was added
    print(dictionary["exit"])
    
    # Print the word that was added
    print(dictionary["exit