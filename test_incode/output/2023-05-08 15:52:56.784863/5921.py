#!/usr/bin/python3
numbers = [1,2,3,4,9]
if __name__ == '__main__':
    #A endless loop that opens a list of numbers.
    #Each time the loop runs, it prints the next number in the list.
    #The loop will run until the user enters 0.
    while(True):
        print(numbers.pop())

