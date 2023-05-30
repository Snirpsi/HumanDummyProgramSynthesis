#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that iterates over words or removes fruits. """    
    
    # Define a function that removes fruits.
    def remove_fruits(fruits):
        fruits.remove('apple')
        fruits.remove('orange')
        fruits.remove('banana')
        
    # Iterate over fruits and remove fruits.
    for fruit in fruits:
        remove_fruits(fruit)
        
    # Print the fruit list.
    print(fruits)
    
    # Print the fruit list without fruits.
    print(list(filter(lambda x: x != 'apple', fruits)))
    
    # Print the fruit list without fruits.
    print(list(filter(lambda x: x != 'orange', fruits)))
    
    # Print the fruit list without fruits.
    print(list(filter(lambda x: x != 'banana', fruits)))
    
    # Print the fruit list without fruits.
    print(list(filter(lambda x: x != 'banana', list(filter(lambda x: x != 'apple', fru