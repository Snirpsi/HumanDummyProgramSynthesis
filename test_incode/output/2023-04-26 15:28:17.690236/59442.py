#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that removes fruits or enumerates numbers. """    
    
    # Read in file of fruits and numbers from stdin
    fruits = sys.stdin.read().split()
    numbers = sys.stdin.read().split()
    
    # Remove fruits from the list
    fruits = [x for x in fruits if x not in numbers]
    
    # Print the fruits without duplicates
    for x in fruits:
        print(x)
    
    # Print the numbers without duplicates
    for x in numbers:
        print(x, end='')
    print()
    
    # Print the fruits with duplicates
    for x in fruits:
        if x in numbers:
            print(x, end='')
    print()
    
    # Print the numbers with duplicates
    for x in numbers:
        if x in fruits:
            print(x, end='')
    print()
    
    # Print the fruits with duplicates and numbers
    for x in fruits:
        if x in numbers:
            print(x, end='')
        for y in numbers:
            if x == y:
                print(y, end='')
        print()
    
    # Print the numbers with duplicates and numbers
    for x in numbers:
        if x in fruits:
            print(x, end='')
        for y in fruits:
            if x == y:
                print(y, end='')
        print()
    
    # Print the fruits with duplicates and numbers and spaces
    for x in fruits:
        if x in numbers:
            print(x, end='')
        for y in numbers:
            if x == y:
                print(y, end='')
        print()
    
    # Print the numbers with duplicates and numbers and spaces
    for x in numbers:
        if x in fruits:
            print(x, end='')
        for y in fruits:
            if x == y:
                print(y, end='')
        print()
    
    # Print the fruits with duplicates and numbers and spaces and spaces
    for x in fruits:
        if x in numbers:
            print(x, end='')
        for y in numbers:
            if x == y:
                print(y, end='')
        print()
    
    # Print the numbers with duplicates and numbers and spaces and spaces
    for x in numbers:
        if x in fruits:
            print(x, end='')
        for y in fruits:
            if x == y:
                print(y, end='')
        print()
    
    # Print the fruits with duplicates and numbers and spaces and spaces
    for x in fruits:
        if x in numbers:
            print(x, end='')
        for y in numbers:
            if x == y:
                print(y, end='')
        print()
    
    # Print the numbers with duplicates and numbers and spaces and spaces
    for x in numbers:
        if x in fruits:
            print(x, end='')
        for y in fruits:
            if x == y:
                print(y, end='')
        print()
    
    # Print the fruits with duplicates and numbers and spaces and 