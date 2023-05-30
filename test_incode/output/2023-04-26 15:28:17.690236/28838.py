#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores fruits and converts user input. """    
    while True:
        fruit = input("Enter a fruit: ")
        if fruit == "quit":
            break
        else:
            fruits.append(fruit)
    print("The fruit list is now:")
    print(fruits)
    print("The fruit list was converted to:")
    print(fruits.