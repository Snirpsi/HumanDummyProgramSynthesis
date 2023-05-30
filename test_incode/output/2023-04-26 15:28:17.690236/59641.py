#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that returns user input. """    
    while True:
        user_input = input("Enter your choice: ")
        if user_input == "quit":
            break
        else:
            print(user_input)
