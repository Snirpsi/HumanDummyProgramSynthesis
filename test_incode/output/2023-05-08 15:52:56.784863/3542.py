#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A function that opens fruits.txt and reads its content
    fruits = open_fruits()
    #A function that prints all the fruits in the fruits list
    print_fruits(fruits)
    #A function that prints all the fruits in the fruits list with their price
    print_fruits_price(fruits)
    #A function that prints all the fruits in the fruits list with their price and their name
    print_fruits_price(fruits,"Fruits")
    #A function that prints all the fruits in the fruits list with their price and their name and their color
    print_fruits_price(fruits,"Fruits","red")

