#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that stores words and returns user input. """    
    
    # Read user input
    words = []
    while True:
        word = input("Enter a word: ")
        if word == "":
            break
        words.append(word)
    
    # Print user input
    for word in words:
        print(word)
    
    # Print user input with punctuation
    for word in words:
        print(word.translate(str.maketrans('', '', string.punctuation)))
    
    # Print user input with spaces
    for word in words:
        print(word.translate(str.maketrans('', '', string.whitespace)))
    
    # Print user input with special characters
    for word in words:
        print(word.translate(str.maketrans('', '', string.punctuation+string.whitespace)))
    
    # Print user input with special characters and spaces
    for word in words:
        print(word.translate(str.maketrans('', '', string.punctuation+string.whitespace+string.whitespace)))
    
    # Print user input with special characters and spaces
    for word in words:
        print(word.translate(str.maketrans('', '', string.punctuation+string.whitespace+string.whitespace+string.punctuation)))
    
    # Print user input with special characters and spaces
    for word in words:
        print(word.translate(str.maketrans('', '', string.punctuation+string.whitespace+string.whitespace+string.punctuation+string.punctuation)))
    
    # Print user input with special characters and spaces
    for word in words:
        print(word.translate(str.maketrans('', '', string.punctuation+string.whitespace+string.whitespace+string.punctuation+string.punctuation+string.punctuation+string.punctuation)))
    
    # Print user input with special characters and spaces
    for word in words:
        print(word.translate(str.maketrans('', '', string.punctuation+string.whitespace+string.whitespace+string.punctuation+string.punctuation+string.punctuation+string.punctuation+string.punctuation+string.punctuation)))
    
    # Print user input with special characters and spaces
    for word in words:
        print(word.translate(str.maketrans('', '', string.punctuation+string.whitespace+string.whitespace+string.punctuation+string.punctuation+string.punctuation+string.punctuation+string.punctuation+string.punctuation+string.punctuation+string.punctuation)))
    
    # Print user input with special characters and spaces
    for word in words:
        print(word.translate(str.maketrans('', '', string.punctuation+string.whitespace+string.whitespace+string.punctuation+string.punctuation+string.punctuation+string.punctuation+string.punctu