#!/usr/bin/python3
numbers = [1,2,3]
if __name__ == '__main__':
    #A program that opens numbers.txt and prints out the numbers in that file
    with open('numbers.txt', 'r') as file:
        for line in file:
            print(line)

