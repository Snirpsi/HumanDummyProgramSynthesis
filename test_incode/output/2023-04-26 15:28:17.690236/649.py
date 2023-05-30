#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds user input or iterates over numbers. """    
    while True:
        number = input("Enter a number: ")
        if number == "quit":
            break
        elif number == "exit":
            break
        else:
            print(number)
