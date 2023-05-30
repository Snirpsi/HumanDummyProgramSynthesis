#!/usr/bin/python3
numbers = [1,2,3]
if __name__ == '__main__':
    #A function that opens numbers.txt and prints its content
    numbers_file = open(numbers, 'r')
    numbers_text = numbers_file.read()
    print(numbers_text)
    numbers_file.close()

