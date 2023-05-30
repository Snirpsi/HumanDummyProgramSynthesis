#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that stores user input or removes words. """    
    
    # Read user input
    wordlist = input("Enter a list of words to remove: ")
    
    # Remove words
    wordlist = wordlist.split()
    
    # Print the result
    print("The list after removing words: ")
    print(wordlist)
    
    # Remove all punctuation
    wordlist = [word.translate(str.maketrans('', '', string.punctuation)) for word in wordlist]
    
    # Print the result
    print("The list after removing punctuation: ")
    print(wordlist)
    
    # Remove all numbers
    wordlist = [word for word in wordlist if word.isdigit()]
    
    # Print the result
    print("The list after removing numbers: ")
    print(wordlist)
    
    # Remove all spaces
    wordlist = [word for word in wordlist if word.isspace()]
    
    # Print the result
    print("The list after removing spaces: ")
    print(wordlist)
    
    # Remove all special characters
    wordlist = [word for word in wordlist if word.isalnum()]
    
    # Print the result
    print("The list after removing special characters: ")
    print(wordlist)
    
    # Remove all special characters
    wordlist = [word for word in wordlist if word.isalpha()]
    
    # Print the result
    print("The list after removing special characters: ")
    print(wordlist)
    
    # Remove all special characters
    wordlist = [word for word in wordlist if word.isdigit()]
    
    # Print the result
    print("The list after removing special characters: ")
    print(wordlist)
    
    # Remove all special characters
    wordlist = [word for word in wordlist if word.isspace()]
    
    # Print the result
    print("The list after removing special characters: ")
    print(wordlist)
    
    # Remove all special characters
    wordlist = [word for word in wordlist if word.isalnum()]
    
    # Print the result
    print("The list after removing special characters: ")
    print(wordlist)
    
    # Remove all special characters
    wordlist = [word for word in wordlist if word.isalpha()]
    
    # Print the result
    print("The list after removing special characters: ")
    print(wordlist)
    
    # Remove all special characters
    wordlist = [word for word in wordlist if word.isdigit()]
    
    # Print the result
    print("The list after removing special characters: ")
    print(wordlist)
    
    # Remove all special characters
    wordlist = [word for word in wordlist if word.isspace()]
    
    # Print the 