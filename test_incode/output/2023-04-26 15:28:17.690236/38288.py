#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores a list of numbers and stores a list of words. """    
    numbers = []
    words = []
    while True:
        number = input("Enter a number: ")
        numbers.append(number)
        word = input("Enter a word: ")
        words.append(word)
        if len(words) == 3:
            break
    print("The numbers 