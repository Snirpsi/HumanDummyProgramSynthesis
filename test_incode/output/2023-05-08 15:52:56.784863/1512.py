#!/usr/bin/python3
numbers = [1,2,3]
if __name__ == '__main__':
    #A program that opens numbers.txt and prints all the numbers from 1 to 3
    with open('numbers.txt', 'r') as numbers:
        for line in numbers:
            print(line)

