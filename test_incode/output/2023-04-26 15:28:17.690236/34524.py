#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts words and iterates over numbers. """    
    while True:
        word = input("Enter a word: ")
        number = int(input("Enter a number: "))
        if word == "quit":
            break
        elif word == "exit":
            break
        else:
            print(word + " " + str(number))
