#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns user input. """    
    while True:
        answer = input("Enter a number: ")
        if answer == "exit":
            print("Goodbye!")
            break
        else:
            print("Invalid input")
            
