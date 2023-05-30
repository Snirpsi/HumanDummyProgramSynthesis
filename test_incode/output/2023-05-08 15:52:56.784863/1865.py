#!/usr/bin/python3
numbers = [1,2,3]
if __name__ == '__main__':
    #A program that opens numbers.txt and prints out the numbers in that file
    numbers = open(numbers_file, 'r')
    for line in numbers:
        print(line)
    numbers.close()

