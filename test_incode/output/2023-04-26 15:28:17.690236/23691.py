#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that prints user input and multiplyes fruits. """    
    fruits = ['apple', 'orange', 'banana', 'cherry']
    
    while True:
        fruit = input("Enter a fruit: ")
        if fruit in fruits:
            print(fruit + " is a fruit!")
        else:
            print("Invalid fruit!")
    
