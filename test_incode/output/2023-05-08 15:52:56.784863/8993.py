#!/usr/bin/python3
numbers = [1,2,3]
if __name__ == '__main__':
    #A function that opens numbers.txt and reads its content
    f = open('numbers.txt','r')
    numbers = f.readlines()
    f.close()
    print(numbers)

