#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A program that opens fruits.txt and prints out the fruit names and prices.
    with open('fruits.txt', 'r') as f:
        for line in f:
            fruit = line.strip()
            price = float(line.split('\t')[1])
            print(fruit, price)
            

