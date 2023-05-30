#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts user input and calculates numbers. """    
    while True:
        number = input("Enter a number: ")
        number = int(number)
        
        if number > 1000:
            print("Sorry, your number is too large.")
        elif number < 1:
            print("Sorry, your number is too small.")
        else:
            answer = number * number
            print("Your answer is", answer)
        
