#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds user input. """    
    while True:
        print("Enter your name: ")
        name = input()
        print("Hello", name)
        print("How are you?")
        answer = input()
        print("Goodbye", name)
        print("Thanks for playing!")
        print("Goodbye")
        break
    
