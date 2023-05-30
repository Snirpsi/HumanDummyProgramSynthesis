#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts numbers. """    
    
    # Get the input from the user
    number = input("Enter a number: ")
    
    # Convert the number to a string
    number = str(number)
    
    # Print the number as a string
    print(number)
    
    # Print the number as a float
    print(float(number))
    
    # Print the number as a integer
    print(int(number))
    
    # Print the number as a boolean
    print(bool(number))
    
    # Print the number as a list
    print(list(number))
    
    # Print the number as a tuple
    print(tuple(number))
    
    # Print the number as a set
    print(set(number))
    
    # Print the number as a frozenset
    print(frozenset(number))
    
    # Print the number as a dict
    print(dict(number))
    
    # Print the number as a defaultdict
    print(defaultdict(int))
    
    # Print the number as a Counter
    print(Counter(number))
    
    # Print the number as a OrderedDict
    print(OrderedDict(number))
    
    # Print the number as a Counter
    print(Counter({1:2, 3:4, 5:6}))
    
    # Print the number as a OrderedDict
    print(OrderedDict({1:2, 3:4, 5:6}))
    
    # Print the number as a Counter
    print(Counter({1:2, 3:4, 5:6}, 