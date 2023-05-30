#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A program that opens fruits.txt and prints them out in reverse order
    with open('fruits.txt', 'r') as f:
        lines = f.readlines()
    for line in reversed(lines):
        print(line)
        #print(line.rstrip())

