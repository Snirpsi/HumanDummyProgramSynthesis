#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A function that converts fruits.txt into list
    fruits = read_fruits()
    #A function that prints fruits list
    print_fruits(fruits)
    #A function that prints fruits list with their count
    print_fruits_count(fruits)

