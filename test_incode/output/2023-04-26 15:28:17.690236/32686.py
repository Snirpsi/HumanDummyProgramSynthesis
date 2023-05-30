#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts user input. """    
    while True:
        answer = input("Enter a number: ")
        answer = int(answer)
        if answer > 0 and answer < 10:
            print("The number you entered is {}!".format(answer))
        else:
            print("Sorry, that number is not in the correct range.")
