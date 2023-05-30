#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over numbers or converts words. """    
    while True:
        number = int(input("Enter a number: "))
        word = input("Enter a word: ")
        if word == "quit":
            break
        else:
            print(number, word)
