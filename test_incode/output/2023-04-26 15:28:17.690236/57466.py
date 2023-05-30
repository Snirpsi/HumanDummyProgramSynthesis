#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes fruits. """    
    while True:
        fruits = input("Enter fruits: ").split()
        for fruit in fruits:
            if fruit not in fruits:
                print(fruit)
                break
        else:
            print("No fruit left.")
            break
