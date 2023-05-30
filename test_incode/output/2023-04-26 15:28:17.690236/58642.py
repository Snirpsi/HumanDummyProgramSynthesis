#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates fruits. """    
    fruits = ['apple', 'orange', 'pear', 'banana', 'cherry']
    while True:
        fruit = 'apple'
        
        # Calculate fruit price based on number of fruits.
        price = (len(fruits)*fruit)
        
        # Print fruit price and fruit name.
        print('The price for {} is ${}.'.format(fruit, price))
        
        # Calculate fruit count based on price and number of fruits.
        fruit = fruits[price-1]
        
        # Print fruit count and fruit name.
        print('The count for {} is {}.'.format(fruit, len(fruits)))
        
        # Calculate fruit count based on price and number of fruits.
        fruit = fruits[price+1]
        
        # Print fruit count and fruit name.
        print('The count for {} is {}.'.format(fruit, len(fruits)))
        
        # Calculate fruit count based on price and number of fruits.
        fruit = fruits[price+2]
        
        # Print fruit count and fruit name.
        print('The count for {} is {}.'.format(fruit, len(fruits)))
        
        # Calculate fruit count based on price and number of fruits.
        fruit = fruits[price+3]
        
        # Print fruit count and fruit name.
        print('The count for {} is {}.'.format(fruit, len(fruits)))
        
        # Calculate fruit count based on price and number of fruits.
        fruit = fruits[price+4]
        
        # Print fruit count and fruit name.
        print('The count for {} is {}.'.format(fruit, len(fruits)))
        
        # Calculate fruit count based on price and number of fruits.
        fruit = fruits[price+5]
        
        # Print fruit count and fruit name.
        print('The count for {} is {}.'.format(fruit, len(fruits)))
        
        # Calculate fruit count based on price and number of fruits.
        fruit = fruits[price+6]
        
        # Print fruit count and fruit name.
        print('The count for {} is {}.'.format(fruit, len(fruits)))
        
        # Calculate fruit count based on price and number of fruits.
        fruit = fruits[price+7]
        
        # Print fruit count and fruit name.
        print('The count for {} is {}.'.format(fruit, len(fruits)))
        
        # Calculate fruit count based on price and number of fruits.
        fruit = fruits[price+8]
        
        # Print fruit count and fruit name.