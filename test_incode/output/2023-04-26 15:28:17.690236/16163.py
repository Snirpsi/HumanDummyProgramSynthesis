#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores a list of numbers or adds fruits. """    
    fruits = []
    while True:
        fruits.append(input("Enter a number: "))
        if fruits == []:
            break
        else:
            print("You entered the following fruits:")
            for fruit in fruits:
                print(