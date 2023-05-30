#!/usr/bin/python3
numbers = [1,2,3]
if __name__ == '__main__':
    #A function that opens numbers.txt and reads its contents into a list
    numbers = open(numbers_filename).readlines()
    #A function that prints out the contents of the list
    print(numbers)

