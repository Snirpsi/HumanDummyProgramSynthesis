#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over user input or opens fruits. """    
    while True:
        fruit = input("Enter a fruit name: ")
        if fruit == 'quit':
            break
        else:
            print("You chose " + fruit)
