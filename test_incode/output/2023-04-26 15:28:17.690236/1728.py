#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that calculates user input and removes words. """    
    
    # Get the user input
    sentence = input('Enter a sentence: ')
    
    # Remove all non-alphabetic characters
    sentence = sentence.translate(str.maketrans('', '', string.punctuation))
    
    # Print the result
    print(sentence)
    
    # Print the length of sentence
    print(len(sentence))
    
    # Print the length of sentence in characters
    print(len(sentence.upper()))
    
    # Print the length of sentence in words
    print(len(sentence.split()))
    
    # Print the length of sentence in words and characters
    print(len(sentence.split()) + len(sentence.upper()))
    
    # Print the length of sentence in words and characters
    print(len(sentence.split()) + len(sentence.upper().split()))
    
    # Print the length of sentence in words and characters and spaces
    print(len(sentence.split()) + len(sentence.upper().split()) + len(sentence.split()) + len(sentence.upper().split()) + len(sentence.split()) + len(sentence.upper().split()) + len(sentence.split()) + len(sentence.upper().split()) + len(sentence.split()) + len(sentence.upper().split()) + len(sentence.split()) + len(sentence.upper().split()) + len(sentence.split()) + len(sentence.upper().split()) + len(sentence.split()) + len(sentence.upper().split()) + len(sentence.split()) + len(sentence.upper().split()) + len(sentence.split()) + len(sentence.upper().split()) + len(sentence.split()) + len(sentence.upper().split()) + len(sentence.split()) + len(sentence.upper().split()) + len(sentence.split()) + len(sentence.upper().split()) + len(sentence.split()) + len(sentence.upper().split()) + len(sentence.split()) + len(sentence.upper().split()) + len(sentence.split()) + len(sentence.upper().split()) + len(sentence.split()) + len(sentence.upper().split()) + len(sentence.split()) + len(sentence.upper().split()) + len(sentence.split()) + len(sentence.upper().split()) + len(sentence.split()) + len(sentence.upper().split()) + len(sentence.split()) + len(sentence.upper().split()) + len(sentence.split()) + len(sentence.upper().split()) + len(sentence.split()) + len(sentence.upper().split()) + len(sentence.split()) + len(sentence.upper().split()) + len(sentence.split()) + len(sentence.upper().split()) + len(sentence.split()) + len(sentence.upper().split()) + len(sentence.split()) + len(sentence.upper().split()) + len(sentence.split()) + len(sentence.upper().split()) + len(sentence.split()) + len(sentence.upper().split()) + len(sentence.split()) + len(sentence.upper().split()) + len(sentence.split()) + len(sentence.upper().split()) + len(sentence.split()) + len(sentence.upper().split()) + len(sentence.split()) + len(sentence.upper().split()) + len(sentence.split()) + len(sentence.upper().split()) + len(sentence.split()) + len(sentence.upper().split()