#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores words or prints a port. """    
    while True:
        word = input("Enter a word: ")
        if word == "quit":
            break
        elif word == "help":
            print("\nAvailable commands:")
            print("\tquit: quit the program")
            print("\thelp: print this message")
        else:
            print(word)
