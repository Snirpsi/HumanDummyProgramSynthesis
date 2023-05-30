#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens fruits and iterates over user input. """    
    
    # Open the fruits file
    fruits = open('fruits.txt', 'r')
    
    # Iterate over the fruits file
    for line in fruits:
        
        # Split the fruit name from the fruit price
        fruit, price = line.split('\t')
        
        # Print the fruit name and price
        print('Fruit ' + fruit + ' is $' + price)
        
    # Close the fruits file
    fruits.close()
    
