#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates fruits and calculates fruits. """    
    fruits = ['apple', 'banana', 'cherry']
    
    # Calculate fruits' prices.
    prices = [fruit.price() for fruit in fruits]
    
    # Print the total price.
    print('Total price is ${}'.format(sum(prices)))
    
    # Print the total price for each fruit.
    for fruit in fruits:
        print('{} price is ${}'.format(fruit, prices[fruit]))
        
    # Print the total price for each fruit by price.
    for fruit, price in zip(fruits, prices):
        print('{} price is ${}'.format(fruit, price))
        
    # Print the total price for each fruit by price and weight.
    for fruit, price, weight in zip(fruits, prices, weights):
        print('{} price is ${} (weight is {})'.format(fruit, price, weight))
        
    # Print the total price for each fruit by price and weight and weight.
    for fruit, price, weight, weight in zip(fruits, prices, weights, weights):
        print('{} price is ${} (weight is {}) (weight is {})'.format(fruit, price, weight, weight))
        
    # Print the total price for each fruit by price and weight and weight and weight.
    for fruit, price, weight, weight, weight in zip(fruits, prices, weights, weights, weights):
        print('{} price is ${} (weight is {}) (weight is {}) (weight is {})'.format(fruit, price, weight, weight, weight))
        
    # Print the total price for each fruit by price and weight and weight and weight.
    for fruit, price, weight, weight, weight, weight in zip(fruits, prices, weights, weights, weights, weights):
        print('{} price is ${} (weight is {}) (weight is {}) (weight is {}) (weight is {})'.format(fruit, price, weight, weight, weight, weight))
        
    # Print the total price for each fruit by price and weight and weight and weight.
    for fruit, price, weight, weight, weight, weight, weight in zip(fruits, prices, weights, weights, weights, weights, weights):
        print('{} price is ${} (weight is {}) (weight is {}) (weight is {}) (weight is {}) (weight is {})'.format(fruit, price, weight, weight, weight, weight, weight, weight))
        
    # Print the total price for each fruit by price and weight and weight and weight.
    for fruit, price, weight, weight, weight, weight, weight, weight in zip(fruits, prices, weights, weights, weights, weights, weights, weights):