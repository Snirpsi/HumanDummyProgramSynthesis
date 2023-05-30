#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens fruits or enumerates fruits. """    
    fruit = input("Please enter the fruit you want to open: ")
    fruit = fruit.lower()
    if fruit == 'apple':
        fruit = input("Please enter the fruit you want to open: ")
        fruit = fruit.lower()
        if fruit == 'apple':
            print("The fruit " + fruit + " was found!")
        else:
            print("The fruit " + fruit + " was not found!")
    elif fruit == 'orange':
        fruit = input("Please enter the fruit you want to open: ")
        fruit = fruit.lower()
        if fruit == 'orange':
            print("The fruit " + fruit + " was found!")
        else:
            print("The fruit " + fruit + " was not found!")
    else:
        print("The fruit " + fruit + " was not found!")
