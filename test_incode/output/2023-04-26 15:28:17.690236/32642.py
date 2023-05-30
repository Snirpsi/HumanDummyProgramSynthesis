#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts fruits or removes all ports. """    
    while True:
        fruits = input("Enter fruits: ").lower()
        if fruits == 'quit':
            break
        else:
            fruits = fruits.split()
            fruits = [x.title() for x in fruits]
            fruits.sort()
            fruits = ' '.join(fruits)
            print(