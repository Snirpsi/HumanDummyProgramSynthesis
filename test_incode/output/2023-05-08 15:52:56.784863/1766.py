#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A endless loop that opens fruits.txt and prints them one by one
    with open('fruits.txt', 'r') as file:
        for line in file:
            print(line)
            

