#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints fruits or returns user input. """    
    while True:
        print("Type 'quit' to exit.")
        fruit = input("Enter a fruit: ")
        if fruit == "quit":
            break
        else:
            print(fruit)
