#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that calculates fruits. """    
    
    # Get the number of fruits.
    fruits = input("How many fruits do you have? ")
    
    # Calculate the number of apples.
    apples = fruits * 2
    
    # Calculate the number of oranges.
    oranges = fruits * 3
    
    # Calculate the number of bananas.
    bananas = fruits * 4
    
    # Calculate the number of kiwis.
    kiwis  = fruits * 5
    
    # Print the results.
    print("You have {} apples, {} oranges, {} bananas and {} kiwis.".format(apples, oranges, bananas, kiwis))
    
