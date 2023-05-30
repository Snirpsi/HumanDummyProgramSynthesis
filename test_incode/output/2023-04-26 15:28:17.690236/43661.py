#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates fruits. """    
    fruits = []
    while True:
        fruits.append(input("Enter a fruit: "))
        if len(fruits) == 0:
            break
    print("The fruits are {}".format(