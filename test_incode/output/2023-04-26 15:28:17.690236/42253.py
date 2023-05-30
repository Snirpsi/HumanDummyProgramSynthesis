#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns numbers or prints fruits. """    
    while True:
        fruits = ['apple', 'orange', 'banana', 'cherry']
        
        # Print the fruits one by one
        for fruit in fruits:
            print(fruit)
        
        # Return numbers or print a message
        if fruits == 'apple':
            print('The fruit is apple!')
        elif fruits == 'orange':
            print('The fruit is orange!')
        elif fruits == 'banana':
            print('The fruit is banana!')
        elif fruits == 'cherry':
            print('The fruit is cherry!')
        else:
            print('The fruit is neither apple nor orange!')
        
        # Exit the loop
        break
    
    # Print the endless loop
    print('The endless loop has ended!')
    
    # Exit the program
    exit()
    
