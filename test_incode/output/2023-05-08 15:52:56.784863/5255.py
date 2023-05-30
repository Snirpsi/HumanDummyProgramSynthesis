#!/usr/bin/python3
numbers = [1,2,3,4,9]
if __name__ == '__main__':
    #A function that opens a list of numbers.
    #It then prints them out in reverse order.
    numbers = openFile()
    print(numbers)
    numbers.close()

