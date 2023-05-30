#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens user input or calculates numbers. """    
    
    number = int(input("Enter a number: "))
    
    if number > 10:
        print("Too big!")
    elif number < 1:
        print("Too small!")
    else:
        print("Correct!")
    
