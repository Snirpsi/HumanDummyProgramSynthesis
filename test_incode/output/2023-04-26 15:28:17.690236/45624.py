#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores user input or stores fruits. """    
    while True:
        fruits = input("Enter your favorite fruit (ex. apple, orange, grape, mango): ")
        if fruits == 'quit':
            break
        else:
            print(