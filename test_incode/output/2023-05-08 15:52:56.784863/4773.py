#!/usr/bin/python3
numbers = [1,2,3]
if __name__ == '__main__':
    #A program that opens numbers.txt and prints the numbers in it.
    numbers = open('numbers.txt','r')
    for line in numbers:
        print(line)
    numbers.close()

