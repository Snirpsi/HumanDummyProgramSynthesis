#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns user input or calculates a list of numbers. """    
    while True:
        number = input("Enter a number: ")
        
        if number == "":
            print("You didn't enter a number.")
        else:
            number = int(number)
            
            if number > 10:
                print("Too high.")
            elif number < 1:
                print("Too low.")
            else:
                print("You entered a number.")
                
