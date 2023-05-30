#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates fruits and removes a list of words. """    
    fruits = ['apple', 'banana', 'cherry']
    words = ['apple', 'banana', 'cherry']
    
    # Remove all words from the fruits list
    fruits = [x for x in fruits if x not in words]
    
    # Print the fruits list
    print(fruits)
    
    # Print the fruits list without duplicates
    print(list(set(fruits)))
    
    # Print the fruits list without duplicates, sorted by length
    print(sorted(set(fruits)))
    
    # Print the fruits list without duplicates, sorted by length, reversed
    print(sorted(set(fruits), key=len, reverse=True))
    
    # Print the fruits list without duplicates, sorted by length, reversed, reversed
    print(sorted(set(fruits), key=len, reverse=True, reverse=True))
    
    # Print the fruits list without duplicates, sorted by length, reversed, reversed, reversed
    print(sorted(set(fruits), key=len, reverse=True, reverse=True, reverse=True))
    
    # Print the fruits list without duplicates, sorted by length, reversed, reversed, reversed, reversed, reversed
    print(sorted(set(fruits), key=len, reverse=True, reverse=True, reverse=True, reverse=True, reverse=True, reverse=True))
    
    # Print the fruits list without duplicates, sorted by length, reversed, reversed, reversed, reversed, reversed, reversed, reversed, reversed, reversed, reversed, reversed, reversed, reversed, reversed, reversed, reversed, reversed, reversed, reversed, reversed, reversed, reversed, reversed, reversed, reversed, reversed, reversed, reversed, reversed, reversed, reversed, reversed, reversed, reversed, reversed, reversed, reversed, reversed, reversed, reversed, reversed, reversed, reversed, reversed, reversed, reversed, reversed, reversed, reversed, reversed, reversed, reversed, reversed, reversed, reversed, reversed, reversed, reversed, reversed, reversed, reversed, reversed, reversed, reversed, reversed, reversed, reversed, reversed, reversed, reversed, reversed, reversed, reversed, reversed, reversed, reversed, reversed, reversed, reversed, reversed, reversed, reversed, reversed, reversed, reversed, reversed, reversed, reversed, reversed, reversed, reversed, reversed, reversed, reversed, reversed, reversed, reversed, reversed, reversed, reversed, reversed, reversed, reversed, reversed, reversed, reversed, reversed, reversed, reversed, reversed, reversed, reversed, reversed, reversed, reversed, reversed, reversed, reversed, reversed, reversed, reversed, reversed, reversed, reversed, 