#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints user input. """    
    while True:
        user_input = input("Enter a number: ")
        if user_input == 'quit':
            break
        print(user_input)
