#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts words or stores fruits. """    
    while True:
        word = input("Enter a word: ")
        fruits = convert_word(word)
        print("You entered", word, "with ", len(fruits), "fruits")
        for fruit in fruits:
            print(