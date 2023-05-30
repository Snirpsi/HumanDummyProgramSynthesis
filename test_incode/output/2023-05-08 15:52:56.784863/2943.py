#!/usr/bin/python3
numbers = [1,2,3]
if __name__ == '__main__':
    #A endless loop that opens numbers.txt and reads its contents into a list.
    with open('numbers.txt', 'r') as f:
        numbers = f.readlines()
    print(numbers)

