#!/usr/bin/python3
numbers = [1,2,3]
if __name__ == '__main__':
    #A function that opens numbers.txt and reads its content
    numbers = open_file('numbers.txt')
    #A function that prints all the numbers in numbers.txt one by one
    print_numbers(numbers)
    #A function that closes numbers.txt and prints its content
    close_file(numbers)

