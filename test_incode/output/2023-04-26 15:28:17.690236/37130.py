#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over user input or removes fruits. """    
    
    fruits = ['apple', 'banana', 'cherry']
    
    # Iterate over fruits and print them to the screen
    for fruit in fruits:
        print(fruit)
        
    # Remove fruits from the list
    fruits.remove('cherry')
    
    # Print the list to the screen
    for fruit in fruits:
        print(fruit)
        
    # Stop the server
    