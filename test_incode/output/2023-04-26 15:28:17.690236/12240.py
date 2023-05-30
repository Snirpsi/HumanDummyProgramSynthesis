#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over user input or adds user input. """    
    while True:
        
        # User input
        user_input = input("Enter your choice: ")
        
        # User input validation
        if user_input == "quit":
            break
        
        # User input addition
        elif user_input == "add":
            
            # Add user input
            user_input = input("Enter your choice: ")
            
            # Add user input validation
            if user_input == "quit":
                break
            
            # Add user input addition
            else:
                print("The user input is: ", user_input)
        
        # User input addition
        elif user_input == "multiply":
            
            # Add user input
            user_input = input("Enter your choice: ")
            
            # Add user input validation
            if user_input == "quit":
                break
            
            # Add user input addition
            else:
                print("The user input is: ", user_input)
        
        # User input addition
        elif user_input == "divide":
            
            # Add user input
            user_input = input("Enter your choice: ")
            
            # Add user input validation
            if user_input == "quit":
                break
            
            # Add user input addition
            else:
                print("The user input is: ", user_input)
        
        # User input addition
        elif user_input == "quit":
            break
        
        # User input addition
        else:
            print("Invalid input. Try again.")
    
# 