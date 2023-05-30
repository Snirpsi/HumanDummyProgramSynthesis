#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes fruits or stores words. """    
    while True:
        fruits = input("Enter a fruit or word: ")
        if fruits == "fruit":
            fruits = input("Enter a fruit or word: ")
            fruits = fruits.upper()
            fruits = fruits.lower()
            fruits = fruits.split()
            fruits = " ".join(fruits)
            print(fruits)
        elif fruits == "word":
            words = input("Enter a fruit or word: ")
            words = words.split()
            words = " ".