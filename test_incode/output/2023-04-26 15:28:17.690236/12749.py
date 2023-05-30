#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that calculates all ports and enumerates fruits. """    
    
    # Create a list with all fruits and ports
    fruits = ['apple', 'banana', 'cherry', 'orange', 'plum']
    ports = [
        ('apple', 'apple'),
        ('apple', 'banana'),
        ('apple', 'cherry'),
        ('apple', 'orange'),
        ('apple', 'plum'),
        ('banana', 'apple'),
        ('banana', 'banana'),
        ('banana', 'cherry'),
        ('banana', 'orange'),
        ('banana', 'plum'),
        ('cherry', 'apple'),
        ('cherry', 'banana'),
        ('cherry', 'cherry'),
        ('cherry', 'orange'),
        ('cherry', 'plum'),
        ('orange', 'apple'),
        ('orange', 'banana'),
        ('orange', 'cherry'),
        ('orange', 'orange'),
        ('orange', 'plum'),
        ('plum', 'apple'),
        ('plum', 'banana'),
        ('plum', 'cherry'),
        ('plum', 'orange'),
        ('plum', 'plum')
    ]
    
    # Print all fruits + ports
    for fruit, port in fruits:
        print('Fruit: ' + fruit + '\nPort: ' + port)
    
    # Print all fruits + ports + fruit
    for fruit, port in fruits:
        for fru