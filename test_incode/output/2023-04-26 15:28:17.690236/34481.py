#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that stores fruits or iterates over words. """    
    
    # Read in words from file
    words = read_file('words.txt')
    
    # Iterate over words and store them in a list
    fruits = []
    for word in words:
        fruits.append(word)
    
    # Print the fruits list
    print(fruits)
    
    # Print the fruits list as a string
    print(fruits.__str__())
    
    # Print the fruits list as a tuple
    print(fruits.__tuple__())
    
    # Print the fruits list as a dictionary
    print(fruits.__dict__())
    
    # Print the fruits list as a set
    print(fruits.__set__())
    
    # Print the fruits list as a frozenset
    print(fruits.__frozenset__())
    
    # Print the fruits list as a frozendict
    print(fruits.__frozendict__())
    
    # Print the fruits list as a frozenlist
    print(fruits.__frozenlist__())
    
    # Print the fruits list as a set
    print(fruits.__set