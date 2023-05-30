#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that removes fruits and stores user input. """    
    
    # Remove fruits
    remove_fruits()
    
    # Store user input
    user_entry = input("Enter a fruit: ")
    
    # Print user input
    print(user_entry)
    
    # Print fruits remaining
    print("Remaining fruits:")
    for fruit in fruits:
        print(fruit)
    
    # Remove fruits again
    remove_