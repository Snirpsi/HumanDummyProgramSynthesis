#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes fruits. """    
    while True:
        fruits = input("Enter fruits: ")
        if fruits == 'quit':
            break
        else:
            fruits = fruits.split()
            for fruit in fruits:
                print(fruit * 