#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes fruits. """    
    while True:
        fruits = input("Enter a fruit: ")
        fruits = fruits.lower()
        if fruits == 'quit':
            break
        else:
            fruits = int(fruits)
            for fruit in fruits:
                print(fruit)
                