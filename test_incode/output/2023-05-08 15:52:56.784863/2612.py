#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A program that opens fruits.txt and prints their names
    with open('fruits.txt', 'r') as file:
        for line in file:
            print(line)

