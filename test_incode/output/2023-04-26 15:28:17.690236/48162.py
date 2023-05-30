#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes user input and opens user input. """    
    while True:
        answer = input("Enter a number: ")
        if answer == "":
            break
        else:
            print(answer * 