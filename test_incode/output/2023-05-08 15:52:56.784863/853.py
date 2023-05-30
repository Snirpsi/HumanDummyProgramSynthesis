#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A program that opens fruits.txt and prints them out in reverse order
    with open('fruits.txt') as fruits:
        for line in fruits:
            print(line[::-1])
            #print(line)

