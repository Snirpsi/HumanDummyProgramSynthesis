#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over user input or converts user input. """    
    while True:
        answer = input("Enter a number: ")
        try:
            answer = int(answer)
        except ValueError:
            print("Invalid input")
        else:
            print("The number you entered is", answer)
