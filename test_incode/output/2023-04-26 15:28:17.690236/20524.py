#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints fruits. """    
    while True:
        print("Fruits")
        fruits = input("Type a fruit: ")
        if fruits == 'quit':
            break
        else:
            print("You typed: " + fruits)
