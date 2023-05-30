#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts user input. """    
    while True:
        answer = input("Enter a number: ")
        try:
            answer = int(answer)
        except ValueError:
            print("That is not a number")
            continue
        else:
            break
    
    if answer == 