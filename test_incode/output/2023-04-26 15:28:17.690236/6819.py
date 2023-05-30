#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes numbers and adds fruits. """    
    while True:
        fruits = input("Enter fruits: ")
        if fruits == '':
            break
        else:
            fruits = fruits.split()
            for fruit in fruits:
                if fruit not in fruits:
                    fruits.append(fruit)
            for fruit in fruits:
                print(