#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A program that opens fruits.txt and prints them out
    with open('fruits.txt', 'r') as f:
        for line in f:
            print(line)
            

