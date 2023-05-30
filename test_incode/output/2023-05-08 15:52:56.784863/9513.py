#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A function that converts fruits.txt into a list of fruit names
    fruits = read_from_file("fruits.txt")
    fruits_names = []
    for fruit in fruits:
        fruits_names.append(fruit)
    #A function that prints the fruit names
    print_fruits(fruits_names)

