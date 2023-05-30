#!/usr/bin/python3
numbers = [1,2,3]
if __name__ == '__main__':
    #A endless loop that removes numbers.
    #This loop will run forever
    while True:
        numbers.remove(3)
        print(numbers)

