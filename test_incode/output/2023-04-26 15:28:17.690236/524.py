#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that returns user input and converts a list of words. """    
    words = input("Enter a sentence or words: ")
    words = words.split()
    
    sentence = ""
    for word in words:
        sentence += word + " "
    
    sentence = sentence[:-1]
    
    print(sentence)
    
