#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates fruits or opens numbers. """    
    while True:
        fruit = input("Enter a fruit or open a number: ")
        if fruit == "open":
            print("Opening numbers...")
            open_numbers()
        elif fruit == "quit":
            print("Goodbye!")
            break
        else:
            print("Invalid input!")
            
