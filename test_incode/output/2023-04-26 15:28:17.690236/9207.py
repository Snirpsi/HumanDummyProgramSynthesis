#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes numbers and prints words. """    
    while True:
        number = int(input("Enter a number: "))
        word = input("Enter a word: ")
        if number > 0 and number <= 10:
            print(word)
        else:
            print("Invalid number")
