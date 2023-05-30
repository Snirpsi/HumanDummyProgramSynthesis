#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that calculates a port and prints fruits. """    
    port = int(input("Enter a port number: "))
    fruits = input("Enter fruits: ").split()
    for fruit in fruits:
        print(fruit, end=' ')
    print(port)
