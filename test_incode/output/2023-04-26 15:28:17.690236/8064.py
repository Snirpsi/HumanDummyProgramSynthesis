#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds user input. """    
    while True:
        user_input = input("Enter a number: ")
        
        if user_input == "":
            break
        else:
            print(user_input)
            
