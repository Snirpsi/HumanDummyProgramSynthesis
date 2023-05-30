#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A program that opens fruits.txt and prints out the fruit names and prices.
    fruits = open("/Users/james/Desktop/fruits.txt")
    for line in fruits:
        fruit = line.strip()
        fruit = fruit.split(",")
        fruit = fruit[0].strip()
        fruit = fruit[1:]
        fruit = ",".join(fruit)
        print(fruit)
    fruit.close()

