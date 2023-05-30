#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A program that opens fruits.txt and prints out the fruit names and prices.
    fruits = open("fruits.txt","r")
    for line in fruits:
        print(line)
        fruit = line.strip()
        print(fruit)
        price = float(line.split(" ")[1])
        print(fruit,price)
        fruits.close()

