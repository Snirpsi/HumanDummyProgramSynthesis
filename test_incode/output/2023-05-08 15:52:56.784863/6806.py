#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A program that converts fruits.
    #It takes as input the name of the fruit and the number of fruits
    #and prints the number of fruits in the given fruit name.
    fruir = input("Enter the name of the fruit: ")
    fruits = int(input("Enter the number of fruits: "))
    
    if fruir == fruirs[0]:
        print("There are {} apples.".format(fruits))
    elif fruir == fruirs[1]:
        print("There are {} bananas.".format(fruits))
    elif fruir == fruirs[2]:
        print("There are {} oranges.".format(fruits))
    else:
        print("Invalid input.")

