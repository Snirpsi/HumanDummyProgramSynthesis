#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens words or calculates a list of numbers. """    
    while True:
        word = input("Enter a word: ")
        if word == "exit":
            break
        elif word == "add":
            number = input("Enter a number: ")
            print(word + " " + number)
        elif word == "multiply":
            number = input("Enter a number: ")
            print(word * number)
        elif word == "divide":
            number = input("Enter a number: ")
            print(word / number)
        else:
            print("Invalid command")
    
