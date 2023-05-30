#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A function that opens fruits.txt and reads its content
    fruits = open_fruits()
    #A function that prints all the fruits in the fruits list
    print_fruits(fruits)
    #A function that prints the fruits in the fruits list with their colors
    print_fruits_with_colors(fruits)

