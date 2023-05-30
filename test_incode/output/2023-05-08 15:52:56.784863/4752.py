#!/usr/bin/python3
numbers = [1,2,3]
if __name__ == '__main__':
    #A function that opens numbers.txt and reads it
    numbers = open(numbers_filename, 'r')
    #A function that prints the contents of numbers.txt to the screen
    print(numbers.read())
    #A function that closes numbers.txt and exits
    numbers.close()

