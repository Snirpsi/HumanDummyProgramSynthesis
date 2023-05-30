#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns a list of words and multiplyes fruits. """    
    words = []
    while True:
        words.append(input("Enter a word: "))
        fruits = input("Enter a fruit: ")
        fruits = fruits.lower()
        if fruits == 'quit':
            break
        else:
            fruits = fruits * 