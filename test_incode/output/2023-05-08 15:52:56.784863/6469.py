#!/usr/bin/python3
numbers = [1,2,3,4,9]
if __name__ == '__main__':
    #A program that opens a list of numbers.
    #The program then prints the numbers in reverse order.
    #The program then closes the list.
    numbers = open(sys.argv[1], 'r')
    numbers_reversed = numbers.readlines()
    numbers.close()
    print(numbers_reversed)
    numbers.close()

