#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates user input or stores user input. """    
    while True:
        try:
            answer = int(input("Enter a number: "))
            break
        except ValueError:
            print("Invalid input. Try again.")
            continue
    
    print("The number you entered is", answer)
    
