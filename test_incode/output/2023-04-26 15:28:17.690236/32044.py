#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints numbers and removes fruits. """    
    while True:
        fruits = input("Enter a fruit (ex. apple, orange, mango): ")
        if fruits == "quit":
            break
        else:
            print(