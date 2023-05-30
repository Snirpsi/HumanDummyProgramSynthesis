#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that removes fruits. """    
    fruits = ['apple', 'banana', 'cherry', 'orange', 'pear', 'strawberry', 'watermelon']
    
    for fruit in fruits:
        if fruit not in ['apple', 'banana', 'cherry', 'orange', 'pear', 'strawberry', 'watermelon']:
            fruits.remove(fruit)
            
    print('The fruits are:', fruits)
    
