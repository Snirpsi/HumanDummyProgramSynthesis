#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts user input and removes numbers. """    
    while True:
        answer = input("Enter a number: ")
        try:
            answer = float(answer)
        except ValueError:
            print("Invalid input")
        else:
            print("The number you entered is", answer)
            
