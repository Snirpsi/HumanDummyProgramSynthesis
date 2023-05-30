#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes user input or removes user input. """    
    while True:
        answer = input("Enter a number: ")
        if answer == "quit":
            break
        else:
            print(answer * 2)
