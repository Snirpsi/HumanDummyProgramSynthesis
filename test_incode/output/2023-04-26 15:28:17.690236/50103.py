#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that removes user input and multiplyes fruits. """    
    
    # Get the user's input
    fruits = input("Enter your favorite fruits: ")
    
    # Remove user input
    fruits = fruits.strip()
    
    # Multiply fruits
    fruits = int(fruits)
    
    # Print the result
    print(fruits)
    
    
