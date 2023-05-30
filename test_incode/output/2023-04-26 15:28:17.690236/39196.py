#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores a list of numbers and multiplyes words. """    
    numbers = []
    words = []
    while True:
        number = input("Enter a number: ")
        if number == "q":
            break
        numbers.append(number)
        word = input("Enter a word: ")
        words.append(word)
    numbers = numbers * len(words)
    print("The numbers are:")
    for number in numbers:
        print(number)
    print("The words are:")
    for word in words:
        print(word)
    print("The product is:")
    for number in numbers:
        number = str(number)
        for word in words:
            word = word + number
        print(word)
    
