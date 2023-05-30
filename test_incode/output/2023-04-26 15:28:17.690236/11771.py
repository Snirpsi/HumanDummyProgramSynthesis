#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes fruits. """    
    while True:
        fruits = input("Enter fruit names to remove: ")
        if fruits == '':
            break
        else:
            fruits = fruits.split()
            for fruit in fruits:
                fruits.remove(fruit)
            print(fruits)
            
