#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints fruits or adds words. """    
    while True:
        print("Type 'quit' to quit")
        fruit = input("Type a fruit: ")
        if fruit == "quit":
            break
        else:
            print("You typed: " + fruit)
            