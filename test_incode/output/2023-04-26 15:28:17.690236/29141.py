#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes fruits or calculates numbers. """    
    fruit = input("Enter a fruit: ")
    number = input("Enter a number: ")
    
    fruit = fruit.lower()
    number = number.lower()
    
    if fruit == "apple" or fruit == "apples":
        print("The fruit is", fruit, "and it's 