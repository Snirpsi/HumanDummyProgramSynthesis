#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes user input or stores fruits. """    
    fruits = input("Enter fruits: ")
    fruits = fruits.split()
    
    for fruit in fruits:
        print(fruit * 2)
    
    print("Done!")
    
