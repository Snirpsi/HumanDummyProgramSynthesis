#!/usr/bin/python3
numbers = [1,2,3,4,9]
if __name__ == '__main__':
    #A endless loop that removes a list of numbers.
    #The loop will run until it reaches the end of the list.
    #The loop will then print out the list that has been removed.
    while(numbers):
        numbers.remove(0)
        print(numbers)

