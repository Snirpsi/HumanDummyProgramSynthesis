#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates fruits. """    
    fruits = ['apple', 'orange', 'banana', 'pear', 'kiwi']
    
    while True:
        fruit = 'apple'
        
        # Print the fruit and the number of times it occurs.
        print('The fruit is', fruit, 'and the number of times it occurs is ', 
              fruits.count(fruit))
        
        # Ask the user for another fruit.
        fruit = input('Enter a fruit: ')
        
        # If the fruit the user entered is invalid, print an error message.
        if fruit not in fruits:
            print('Invalid fruit!')
        else:
            break
    
    # If the user enters quit, the program will exit.
