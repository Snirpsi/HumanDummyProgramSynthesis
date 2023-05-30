#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens words or stores numbers. """    
    while True:
        word = input("Enter a word: ")
        number = input("Enter a number: ")
        if word == "quit":
            break
        elif word == "add":
            number = int(number)
            print(word + " " + number)
        elif word == "store":
            print(word + " " + str(number))
        else:
            print(word + " is not a word")
            
