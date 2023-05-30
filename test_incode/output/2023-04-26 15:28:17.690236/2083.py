#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that adds numbers. """    
    
    numbers = input("Enter a number or enter 'quit': ")
    
    if numbers == "quit":
        print("Goodbye!")
        exit()
    
    numbers = int(numbers)
    
    if numbers < 1:
        print("Please enter a positive number.")
        
    elif numbers > 10:
        print("Please enter a number between 1 and 10.")
        
    else:
        print("The sum of numbers is {}.".format(numbers))
        
