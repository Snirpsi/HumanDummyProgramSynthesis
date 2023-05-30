#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts a list of words and opens numbers. """    
    words = []
    numbers = []
    while True:
        words = input("Enter a word: ")
        numbers = input("Enter a number: ")
        if words == numbers:
            break
        else:
            print("Invalid input")
    
    words.sort()
    numbers.sort()
    
    for word in words:
        if word not in numbers:
            print(word + " is not in numbers")
        else:
            print(word + " is in numbers")
    
    for number in numbers:
        if number not in words:
            print(number + " is not in words")
        else:
            print(number + " is in words")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
