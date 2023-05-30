#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates user input and removes numbers. """    
    while True:
        answer = input("Enter a number: ")
        try:
            answer = int(answer)
        except ValueError:
            print("Please enter a number.")
            continue
        if answer < 0:
            print("Please enter a number greater than 0.")
            continue
        if answer > 10:
            print("Please enter a number less than 10.")
            continue
        if answer == 10:
            break
        else:
            print("You entered 